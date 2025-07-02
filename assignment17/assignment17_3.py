import schedule
import time

def coding():
    print("Do Coding..!")

schedule.every(30).minutes.do(coding)

while True:
    schedule.run_pending()
    time.sleep(1)