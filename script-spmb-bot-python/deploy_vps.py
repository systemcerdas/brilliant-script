import paramiko
import time
import os

def load_credentials():
    creds = {}
    with open(".cred", "r") as f:
        for line in f:
            if "=" in line:
                key, val = line.strip().split("=", 1)
                creds[key.strip()] = val.strip().strip("'").strip('"')
    return creds

def run_command(ssh, cmd):
    print(f"\n[VPS] Menjalankan: {cmd}")
    stdin, stdout, stderr = ssh.exec_command(cmd)
    
    # Tunggu command selesai dan print output secara real-time
    exit_status = stdout.channel.recv_exit_status()
    out = stdout.read().decode('utf-8')
    err = stderr.read().decode('utf-8')
    
    if out: print(out.strip().encode('ascii', 'replace').decode('ascii'))
    if err: print(f"ERROR: {err.strip().encode('ascii', 'replace').decode('ascii')}")
    print(f"[VPS] Selesai dengan kode: {exit_status}")
    return exit_status

def main():
    creds = load_credentials()
    vps_ip = creds.get('VPS_IP')
    vps_user = creds.get('VPS_USER')
    vps_pass = creds.get('VPS_PASS')
    pac = creds.get('pac', '')

    print("Menghubungkan ke VPS...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(hostname=vps_ip, username=vps_user, password=vps_pass, timeout=10)
        print("Berhasil terhubung ke VPS!")

        # Install system dependencies (git, tmux, python3-venv)
        run_command(ssh, "sudo apt-get update && sudo apt-get install -y git tmux python3-pip python3-venv")

        repo_url = f"https://{pac}@github.com/BrillianLabs/BrillianScript.git" if pac else "https://github.com/BrillianLabs/BrillianScript.git"
        
        # Setup Repositori
        repo_cmd = f"""
        if [ -d "BrillianScript" ]; then
            cd BrillianScript
            git remote set-url origin {repo_url}
            git pull origin master
        else
            git clone {repo_url}
        fi
        """
        run_command(ssh, repo_cmd)

        # Upload file .data asli dari komputer lokal agar ada credentials
        local_data_path = ".data"
        if os.path.exists(local_data_path):
            print("\n[VPS] Mengunggah file .data ke server...")
            sftp = ssh.open_sftp()
            # pastikan folder di server sudah ada
            remote_path = "/home/ubuntu/BrillianScript/script-spmb-bot-python/.data"
            try:
                sftp.put(local_data_path, remote_path)
                print("[VPS] Berhasil mengunggah .data")
            except Exception as e:
                print(f"[VPS] Gagal mengunggah .data: {e}")
            finally:
                sftp.close()
        else:
            print("[VPS] File .data tidak ditemukan di lokal, pastikan sudah dibuat.")

        # Setup Virtual Environment dan dependencies Python di VPS
        setup_python_cmd = """
        cd /home/ubuntu/BrillianScript/script-spmb-bot-python
        python3 -m venv .venv
        source .venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
        playwright install chromium
        playwright install-deps chromium
        """
        run_command(ssh, setup_python_cmd)

        # Menyiapkan Systemd Service untuk Watcher & Web Dashboard (Gunicorn)
        service_cmd = """
        cd /home/ubuntu/BrillianScript/script-spmb-bot-python
        
        # 1. Service untuk SPMB Watcher
        cat << 'EOF' | sudo tee /etc/systemd/system/spmb_watcher.service
[Unit]
Description=SPMB Bot Watcher
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/BrillianScript/script-spmb-bot-python
Environment="PATH=/home/ubuntu/BrillianScript/script-spmb-bot-python/.venv/bin"
ExecStart=/home/ubuntu/BrillianScript/script-spmb-bot-python/.venv/bin/python spmb_watcher.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

        # 2. Service untuk Gunicorn Web Dashboard
        cat << 'EOF' | sudo tee /etc/systemd/system/spmb_web.service
[Unit]
Description=SPMB Web Dashboard (Gunicorn)
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/BrillianScript/script-spmb-bot-python
Environment="PATH=/home/ubuntu/BrillianScript/script-spmb-bot-python/.venv/bin"
ExecStart=/home/ubuntu/BrillianScript/script-spmb-bot-python/.venv/bin/gunicorn -w 1 -b 0.0.0.0:8000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF

        # Reload dan Start Services
        sudo systemctl daemon-reload
        sudo systemctl enable spmb_watcher
        sudo systemctl enable spmb_web
        sudo systemctl restart spmb_watcher
        sudo systemctl restart spmb_web
        """
        run_command(ssh, service_cmd)

        print("\n==============================================")
        print("DEPLOYMENT SELESAI!")
        print("Bot Watcher & Web Dashboard telah di-deploy sebagai SYSTEMD SERVICE.")
        print(f"Buka Dashboard di browser: http://{vps_ip}:8000")
        print("Cek status service di server:")
        print("  sudo systemctl status spmb_watcher")
        print("  sudo systemctl status spmb_web")
        print("==============================================")

    except Exception as e:
        print(f"Gagal koneksi atau eksekusi: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    main()
