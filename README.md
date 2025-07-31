<h1>Sistem Monitoring Bandwidth</h1>

<p>📁 File:</p>
- send_bandwidth_to_firebase.py → Kirim data ke Firebase tiap 5 detik
- generate_daily_summary.py     → Buat laporan total harian ke Firebase
<p></p>
- config.ini                    → Konfigurasi interface & Firebase
- firebase-key.json            → Tambahkan sendiri (dari Firebase service account)
<p></p>
📦 Instalasi:
pip install psutil firebase-admin
<p></p>
🧪 Jalankan monitoring:
python3 send_bandwidth_to_firebase.py
<p></p>
📝 Jalankan laporan harian:
python3 generate_daily_summary.py
<p></p>
💡 Gunakan cron atau systemd untuk otomatisasi.
