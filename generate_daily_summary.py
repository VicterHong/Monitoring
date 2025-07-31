import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

cred = credentials.Certificate("firebase-key.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://monitoring-bandwith-26c51-default-rtdb.firebaseio.com"
})

ref = db.reference("bandwidth_logs")
today = datetime.now().date()
total_in = total_out = 0

logs = ref.get()
if logs:
    for entry in logs.values():
        ts = datetime.fromisoformat(entry["timestamp"])
        if ts.date() == today:
            total_in += entry.get("download_kbps", 0)
            total_out += entry.get("upload_kbps", 0)

summary_ref = db.reference("daily_summary")
summary_ref.child(today.isoformat()).set({
    "total_in_mbps": round(total_in / 1024 * 8, 2),
    "total_out_mbps": round(total_out / 1024 * 8, 2)
})
print("Laporan harian berhasil dikirim.")
