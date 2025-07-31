=== Sistem Monitoring Bandwidth ===

📁 File:
- send_bandwidth_to_firebase.py → Kirim data ke Firebase tiap 5 detik
- generate_daily_summary.py     → Buat laporan total harian ke Firebase
- config.ini                    → Konfigurasi interface & Firebase
- firebase-key.json             → Tambahkan sendiri (dari Firebase service account)

📦 Instalasi:
pip install psutil firebase-admin

🧪 Jalankan monitoring:
python3 send_bandwidth_to_firebase.py

📝 Jalankan laporan harian:
python3 generate_daily_summary.py

💡 Gunakan cron atau systemd untuk otomatisasi.
