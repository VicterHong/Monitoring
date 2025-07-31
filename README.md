<h1>Sistem Monitoring Bandwidth</h1>

<p>📁 File:</p>
- send_bandwidth_to_firebase.py → Kirim data ke Firebase tiap 5 detik
- generate_daily_summary.py     → Buat laporan total harian ke Firebase

<p>- config.ini </p>                   → Konfigurasi interface & Firebase
- firebase-key.json            → Tambahkan sendiri (dari Firebase service account)

<p>📦 Instalasi:</p> 
pip install psutil firebase-admin

<p>🧪 Jalankan monitoring:</p>
python3 send_bandwidth_to_firebase.py

<p>📝 Jalankan laporan harian:</p>
python3 generate_daily_summary.py

<p>💡 Gunakan cron atau systemd untuk otomatisasi.</p>
