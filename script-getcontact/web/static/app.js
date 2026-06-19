const $ = (id) => document.getElementById(id);

const stepForm = $("step-form");
const stepVerify = $("step-verify");
const stepResult = $("step-result");

$("btn-start").addEventListener("click", startFlow);
$("btn-reset").addEventListener("click", resetFlow);

async function startFlow() {
  hideError("form-error");
  const phone = $("phone").value.trim();

  $("btn-start").disabled = true;
  $("btn-start").textContent = "Memproses...";

  try {
    const res = await post("/api/start", { phone });
    showVerify(res);
  } catch (err) {
    showError("form-error", err.message);
    $("btn-start").disabled = false;
    $("btn-start").textContent = "Mulai Verifikasi";
  }
}

function showVerify(data) {
  stepForm.classList.add("hidden");
  stepVerify.classList.remove("hidden");
  stepResult.classList.add("hidden");

  $("display-phone").textContent = data.phone;
  $("wa-link").href = data.wa_link;
  runCountdown(data.countdown || 10, checkVerification);
}

function runCountdown(seconds, onDone) {
  let left = seconds;
  const bar = $("countdown-bar");
  const label = $("countdown-sec");

  bar.style.width = "100%";
  label.textContent = left;

  const timer = setInterval(() => {
    left -= 1;
    label.textContent = Math.max(left, 0);
    bar.style.width = `${(left / seconds) * 100}%`;

    if (left <= 0) {
      clearInterval(timer);
      onDone();
    }
  }, 1000);
}

async function checkVerification() {
  hideError("verify-error");
  $("countdown-label").textContent = "Mengecek verifikasi...";

  try {
    const res = await post("/api/check", {});
    showResult(res);
  } catch (err) {
    if (err.code === "verify_pending") {
      $("countdown-label").textContent = "Belum terverifikasi, coba lagi...";
      setTimeout(checkVerification, 3000);
      return;
    }
    showError("verify-error", err.message);
  }
}

function showResult(data) {
  stepVerify.classList.add("hidden");
  stepResult.classList.remove("hidden");

  $("tag-count").textContent = data.count;
  const list = $("tag-list");
  list.innerHTML = "";

  if (!data.tags?.length) {
    const li = document.createElement("li");
    li.textContent = "Tidak ada tag ditemukan.";
    list.appendChild(li);
    return;
  }

  data.tags.forEach((tag, i) => {
    const li = document.createElement("li");
    li.textContent = `${i + 1}. ${tag}`;
    list.appendChild(li);
  });
}

function resetFlow() {
  stepForm.classList.remove("hidden");
  stepVerify.classList.add("hidden");
  stepResult.classList.add("hidden");
  $("btn-start").disabled = false;
  $("btn-start").textContent = "Mulai Verifikasi";
  hideError("form-error");
  hideError("verify-error");
}

async function post(url, body) {
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  const data = await res.json();
  if (!data.ok) {
    const err = new Error(data.error || "Terjadi kesalahan.");
    err.code = data.code;
    throw err;
  }
  return data;
}

function showError(id, msg) {
  const el = $(id);
  el.textContent = msg;
  el.classList.remove("hidden");
}

function hideError(id) {
  const el = $(id);
  el.textContent = "";
  el.classList.add("hidden");
}
