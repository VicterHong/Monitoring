<h1>Bandwidth Monitoring System</h1>

<p>📁 Files:</p>
- send_bandwidth_to_firebase.py → Sends data to Firebase every 5 seconds
- generate_daily_summary.py     → Generates a daily summary report to Firebase
<p></p>
- config.ini                    → Interface & Firebase configuration
- firebase-key.json            → Add your own (from Firebase service account)
<p></p>
📦 Installation:<p></p>
pip install psutil firebase-admin
<p></p>
🧪 Run monitoring:<p></p>
python3 send_bandwidth_to_firebase.py
<p></p>
📝 Run daily report:<p></p>
python3 generate_daily_summary.py
<p></p> 
<p></p>💡 Use cron or systemd for automation.
