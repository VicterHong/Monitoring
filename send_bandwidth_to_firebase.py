import psutil
import time
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

cred = credentials.Certificate("firebase-key.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://monitoring-bandwith-26c51-default-rtdb.firebaseio.com"
})

INTERFACE = "eth0"  # Ganti sesuai interface kamu
INTERVAL = 5  # detik

ref = db.reference("bandwidth_logs")
old_sent = psutil.net_io_counters(pernic=True)[INTERFACE].bytes_sent
old_recv = psutil.net_io_counters(pernic=True)[INTERFACE].bytes_recv

while True:
    time.sleep(INTERVAL)
    counters = psutil.net_io_counters(pernic=True)[INTERFACE]
    new_sent = counters.bytes_sent
    new_recv = counters.bytes_recv

    upload_kbps = (new_sent - old_sent) / 1024 / INTERVAL
    download_kbps = (new_recv - old_recv) / 1024 / INTERVAL
    old_sent, old_recv = new_sent, new_recv

    ref.push({
        "timestamp": datetime.now().isoformat(),
        "upload_kbps": round(upload_kbps, 2),
        "download_kbps": round(download_kbps, 2)
    })
