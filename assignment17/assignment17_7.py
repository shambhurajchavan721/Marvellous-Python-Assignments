import schedule
import time
from datetime import datetime
import shutil

def backup():
    shutil.copy("source_file.txt", "backup_file.txt")
    with open("backup_log.txt", "a") as log:
        log.write(f"Backup taken at {datetime.now()}\n")

schedule.every().hour.do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)