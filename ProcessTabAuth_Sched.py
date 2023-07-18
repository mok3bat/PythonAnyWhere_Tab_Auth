import schedule
import time
import subprocess

def run_script():
    subprocess.call(["python3", "/var/www/mok3bat_pythonanywhere_com_wsgi.py"])

# Schedule the script to run every 8 minutes
schedule.every(9).minutes.do(run_script)

# Keep the script running continuously
while True:
    schedule.run_pending()
    time.sleep(9*60+3)
