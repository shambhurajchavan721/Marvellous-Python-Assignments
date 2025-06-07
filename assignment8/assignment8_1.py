import threading
def even_10():
    for i in range(10):
        print("Even:",i*2)

def odd_10():
    for i in range(10):
        print("odd:",i *2 + 1)

def main():

    even = threading.Thread(target=even_10)
    odd  = threading.Thread(target = odd_10)

    even.start()
    odd.start()

    even.join()
    odd.join()

if __name__== "__main__":
    main()