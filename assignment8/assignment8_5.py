import threading

def Display_order():
    for i in range(1,51):
        print(i)

def Display_reverse_order():
    for i in range(50,0,-1):
        print(i)

def main():

    thread1 = threading.Thread(target=Display_order)
    thread2 = threading.Thread(target=Display_reverse_order)

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()
    

if __name__ == "__main__":
    main()