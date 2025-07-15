"""
Scheduler orchestrating periodic tasks.
"""
import schedule
import time
from .export_task import export_data

def run_scheduler():
    schedule.every().day.at("00:00").do(export_data)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()
