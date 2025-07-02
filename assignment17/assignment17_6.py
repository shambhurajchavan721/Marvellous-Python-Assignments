import schedule
import time

def lunch_time():
    print("Lunch Time!")

def wrap_up():
    print("Wrap up work")

schedule.every().day.at("13:00").do(lunch_time)
schedule.every().day.at("18:00").do(wrap_up)

while True:
    schedule.run_pending()
    time.sleep(1)