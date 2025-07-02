import schedule
import time

def task():
    print("Jay Ganesh")

schedule.every(2).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)