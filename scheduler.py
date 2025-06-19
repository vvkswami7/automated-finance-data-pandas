# scheduler.py

import schedule
import time
from datetime import datetime
from main import fetch_stock_data

def job():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[ {now}] Scheduled Job Running...")
    fetch_stock_data("AAPL")

# Run every day at 10:00 AM (you can change the time below)
schedule.every(1).minutes.do(job)

print("[INFO] Scheduler started. Waiting for scheduled time...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
