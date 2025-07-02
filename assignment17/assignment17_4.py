import schedule
import time

def greet():
    print("Namskar...")

schedule.every().day.at("09:00").do(greet)

while True:
    schedule.run_pending()
    time.sleep(1)