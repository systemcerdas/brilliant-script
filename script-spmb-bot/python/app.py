from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    log_path = "spmb_output/watcher.log"
    log_content = "Log belum tersedia..."
    if os.path.exists(log_path):
        with open(log_path, 'r', encoding='utf-8') as f:
            # Ambil 50 baris terakhir biar tidak berat
            lines = f.readlines()
            log_content = "".join(lines[-50:])
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SPMB Bot Dashboard</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; background: #121212; color: #fff; }}
            h1 {{ color: #00ffcc; }}
            pre {{ background: #1e1e1e; padding: 15px; border-radius: 8px; overflow-x: auto; font-size: 14px; border: 1px solid #333; }}
            .img-container {{ display: flex; gap: 20px; flex-wrap: wrap; margin-top: 20px; }}
            .img-card {{ background: #1e1e1e; padding: 10px; border-radius: 8px; border: 1px solid #333; }}
            img {{ max-width: 100%; height: auto; max-height: 500px; }}
        </style>
        <meta http-equiv="refresh" content="30">
    </head>
    <body>
        <h1>🩺 Dashboard SPMB Bot</h1>
        <p>Halaman ini akan me-refresh otomatis setiap 30 detik untuk memantau log terbaru.</p>
        
        <h3>Log Terakhir (50 Baris)</h3>
        <pre>{log_content}</pre>
        
        <h3>Tangkapan Layar Bukti BINGO</h3>
        <div class="img-container">
            <div class="img-card">
                <h4>Bukti Register (Jika dihapus)</h4>
                <img src="/img/SUCCESS_REGISTER.png" alt="Belum ada bukti register" onerror="this.style.display='none'">
            </div>
            <div class="img-card">
                <h4>Bukti Login (Jika diverifikasi)</h4>
                <img src="/img/SUCCESS_LOGIN.png" alt="Belum ada bukti login" onerror="this.style.display='none'">
            </div>
        </div>
    </body>
    </html>
    """
    return html

@app.route('/img/<name>')
def get_img(name):
    path = f"spmb_output/{name}"
    if os.path.exists(path):
        return send_file(path)
    return "Not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
