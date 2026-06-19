"""GetContact web UI — Flask server."""

import os
import secrets

from flask import Flask, jsonify, render_template, session

from getcontact import (
    GetContactError,
    check_verification_and_fetch_tags,
    fetch_session_tokens,
    start_whatsapp_verification,
    validate_phone,
)

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", secrets.token_hex(32))


@app.route("/")
def index():
    return render_template("index.html")


@app.post("/api/start")
def api_start():
    body = _json_body()
    phone = (body.get("phone") or "").strip()

    try:
        validate_phone(phone)
        tokens = fetch_session_tokens()
        verification = start_whatsapp_verification(tokens, phone)
    except GetContactError as exc:
        return _err(str(exc), exc.code, 400)
    except Exception:
        return _err("Gagal menghubungi server GetContact.", "network_error", 502)

    session["tokens"] = {
        "access_token": tokens.access_token,
        "token": tokens.token,
        "hash_value": tokens.hash_value,
    }
    session["phone"] = verification["phone"]

    return jsonify(
        {
            "ok": True,
            "wa_link": verification["wa_link"],
            "phone": verification["phone"],
            "countdown": 10,
        }
    )


@app.post("/api/check")
def api_check():
    tokens_data = session.get("tokens")
    phone = session.get("phone")

    if not tokens_data or not phone:
        return _err("Sesi habis. Mulai ulang dari awal.", "session_expired", 400)

    from getcontact import SessionTokens

    tokens = SessionTokens(**tokens_data)

    try:
        result = check_verification_and_fetch_tags(tokens, phone)
    except GetContactError as exc:
        status = 202 if exc.code == "verify_pending" else 400
        return _err(str(exc), exc.code, status)
    except Exception:
        return _err("Gagal mengambil data tag.", "network_error", 502)

    session.clear()
    return jsonify({"ok": True, **result})


def _json_body():
    from flask import request

    return request.get_json(silent=True) or {}


def _err(message: str, code: str, status: int):
    return jsonify({"ok": False, "error": message, "code": code}), status


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port, debug=True)
