import schedule
import time
from datetime import datetime

def show_datetime():
    print(datetime.now())

schedule.every(1).minutes.do(show_datetime)

while True:
    schedule.run_pending()
    time.sleep(1)