import schedule, time
from src.tasks.export import export_logs
schedule.every().day.at('00:00').do(export_logs)
while True:
    schedule.run_pending()
    time.sleep(1)