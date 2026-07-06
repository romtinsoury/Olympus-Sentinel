# این فایل app.py در پوشه olympus_project است
from flask import Flask, render_template, jsonify
import platform
import os
import psutil

app = Flask(__name__)

# لیست پورت‌های حساس و مشکوک سایبری (شکار تهدیدات)
SUSPICIOUS_PORTS = {
    4444: "Metasploit / Reverse Shell",
    135: "RPC (Potential Lateral Movement)",
    139: "NetBIOS (SMB Attack Risk)",
    445: "SMB (WannaCry / EternalBlue Risk)",
    3389: "RDP (Remote Desktop Scan)",
    5900: "VNC Unauthorized Access",
    23: "Telnet (Unencrypted/Insecure)",
    21: "FTP (Plaintext Credentials)"
}

@app.route('/')
def home():
    return render_template('olympus.html')

@app.route('/api/system')
def get_system_info():
    try:
        username = os.getlogin()
    except Exception:
        username = "Unknown User"

    cpu_percent = psutil.cpu_percent(interval=0.1)
    ram_percent = psutil.virtual_memory().percent

    specs = {
        "username": username,
        "system": platform.system(),
        "release": platform.release(),
        "cpu_usage": cpu_percent,
        "ram_usage": ram_percent
    }
    return jsonify(specs)

@app.route('/api/network')
def get_network_connections():
    connections_list = []
    try:
        for conn in psutil.net_connections(kind='inet'):
            try:
                proc = psutil.Process(conn.pid)
                proc_name = proc.name()
            except (psutil.NoSuchProcess, psutil.AccessDenied, TypeError):
                proc_name = "Unknown"

            local_port = conn.laddr.port if conn.laddr else None
            remote_port = conn.raddr.port if conn.raddr else None
            
            # تحلیل هوشمند ریسک پورت‌ها
            is_suspicious = False
            risk_reason = ""
            
            if local_port in SUSPICIOUS_PORTS:
                is_suspicious = True
                risk_reason = SUSPICIOUS_PORTS[local_port]
            elif remote_port in SUSPICIOUS_PORTS:
                is_suspicious = True
                risk_reason = SUSPICIOUS_PORTS[remote_port]
            elif conn.status == "SYN_SENT":
                is_suspicious = True
                risk_reason = "Port Scanning Activity"

            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "-"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "-"
            
            connections_list.append({
                "type": "TCP" if conn.type == 1 else "UDP",
                "local_address": laddr,
                "foreign_address": raddr,
                "status": conn.status,
                "pid": conn.pid or "-",
                "process_name": proc_name,
                "is_suspicious": is_suspicious,
                "risk_reason": risk_reason
            })
    except Exception as e:
        return jsonify({"error": str(e)})

    # فرستادن ۲۰ اتصال اول جهت حفظ کارایی سیستم
    return jsonify(connections_list[:20])

if __name__ == "__main__":
    app.run(debug=True, port=5000)