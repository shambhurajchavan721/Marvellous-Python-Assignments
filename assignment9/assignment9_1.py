import threading
import time

def Display():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def main():

    thread1 = threading.Thread(target=Display)
    thread2 = threading.Thread(target=Display)
    thread3 = threading.Thread(target=Display)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == "__main__":
    main()