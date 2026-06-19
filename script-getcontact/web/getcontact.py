"""GetContact API client — ported from script/bot.php."""

import re
from dataclasses import dataclass

import requests

UA = (
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"
)
VERIFYKIT_ORIGIN = "https://gtc-manage-widget.verifykit.com"
VERIFYKIT_HEADERS = {
    "user-agent": UA,
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "sec-ch-ua-platform": '"Android"',
    "sec-ch-ua-mobile": "?1",
    "origin": VERIFYKIT_ORIGIN,
    "referer": f"{VERIFYKIT_ORIGIN}/",
}


@dataclass
class SessionTokens:
    access_token: str
    token: str
    hash_value: str


class GetContactError(Exception):
    def __init__(self, message: str, code: str = "error"):
        super().__init__(message)
        self.code = code


def validate_phone(phone: str) -> None:
    if not phone or "0" not in phone:
        raise GetContactError("Nomor WhatsApp harus format Indonesia (mengandung angka 0).", "invalid_phone")


def fetch_session_tokens() -> SessionTokens:
    res = requests.get(
        "https://getcontact.com/id/manage",
        headers={
            "user-agent": UA,
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "upgrade-insecure-requests": "1",
        },
        timeout=30,
        allow_redirects=True,
    )
    res.raise_for_status()
    body = res.text

    # accessToken biasanya hanya di Set-Cookie (PHP pakai CURLOPT_HEADER=1)
    access_token = res.cookies.get("accessToken") or ""
    if not access_token:
        header_blob = "\n".join(f"{k}: {v}" for k, v in res.headers.items())
        access_token = _extract(header_blob, r"accessToken=([^;\s]+)")

    token = _extract(body, r"token=([^&\"'\s]+)")
    hash_value = _extract_hash(body)

    if not all([access_token, token, hash_value]):
        raise GetContactError("Gagal mengambil token dari GetContact.", "token_error")

    return SessionTokens(access_token, token, hash_value)


def start_whatsapp_verification(tokens: SessionTokens, phone: str) -> dict:
    payload = {
        "lang": "id",
        "token": tokens.token,
        "clientHost": "https://getcontact.com",
        "validationType": "whatsapp",
        "countryCode": "id",
        "phoneNumber": phone,
        "deeplink": True,
    }
    res = requests.post(
        "https://widget.verifykit.com/v3.0/start",
        headers=VERIFYKIT_HEADERS,
        json=payload,
        timeout=30,
    )
    data = res.json()

    if "Anda memasukkan nomor telepon yang tidak sah" in res.text:
        raise GetContactError("Nomor WhatsApp tidak valid.", "invalid_phone")

    result = data.get("result") or {}
    validation = result.get("validation") or {}
    phone_info = result.get("phoneNumber") or {}

    link = validation.get("link")
    if not link:
        raise GetContactError("Gagal memulai verifikasi WhatsApp.", "verify_start_failed")

    return {
        "wa_link": link,
        "phone": phone_info.get("phoneNumber", phone),
    }


def check_verification_and_fetch_tags(tokens: SessionTokens, phone: str) -> dict:
    check_res = requests.post(
        "https://widget.verifykit.com/v3.0/check",
        headers=VERIFYKIT_HEADERS,
        json={
            "lang": "id",
            "token": tokens.token,
            "clientHost": "https://getcontact.com",
            "phoneNumber": phone,
            "validationType": "whatsapp",
        },
        timeout=30,
    )
    check_data = check_res.json()

    if "success" not in check_res.text.lower():
        raise GetContactError("Verifikasi WhatsApp belum selesai. Coba lagi setelah kirim pesan.", "verify_pending")

    session_id = (check_data.get("result") or {}).get("validation", {}).get("sessionId")
    if not session_id:
        raise GetContactError("Session verifikasi tidak ditemukan.", "verify_failed")

    validate_res = requests.post(
        "https://getcontact.com/validation-verifykit-check",
        headers={
            "user-agent": UA,
            "referer": "https://getcontact.com/id/manage",
            "cookie": f"lang=id; cookieInform=accept; accessToken={tokens.access_token}",
        },
        data={"hash": tokens.hash_value, "sessionId": session_id},
        timeout=30,
    )

    if "success" not in validate_res.text.lower():
        raise GetContactError("Validasi GetContact gagal.", "validate_failed")

    profile_res = requests.get(
        "https://getcontact.com/id/manage/profile",
        headers={
            "user-agent": UA,
            "cookie": (
                f"lang=id; cookieInform=accept; accessToken={tokens.access_token}"
            ),
        },
        timeout=30,
    )
    tags = parse_profile_tags(profile_res.text)
    return {"count": len(tags), "tags": tags}


def parse_profile_tags(html: str) -> list[str]:
    parts = html.split('<div class="pt-text">')
    tags = []
    for chunk in parts[1:]:
        tag = chunk.split("</div>", 1)[0].strip()
        if tag:
            tags.append(tag)
    return tags


def _extract(text: str, pattern: str) -> str:
    match = re.search(pattern, text)
    return match.group(1) if match else ""


def _extract_hash(text: str) -> str:
    match = re.search(r'"hash":\s*\'([^\']+)\'', text)
    if match:
        return match.group(1)
    match = re.search(r'"hash":\s*"([^"]+)"', text)
    return match.group(1) if match else ""
