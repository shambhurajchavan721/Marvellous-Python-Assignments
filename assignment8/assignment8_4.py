import threading

def Display_small(string1):
    count = 0
    for i in string1:
        if 'a' <= i <= 'z': 
            count += 1

    print("Number of small letters:",count)
    print("Thread name is:",threading.current_thread().name)
    print("thread id of small is:",threading.get_ident())

def Display_capital(string1):
    count = 0
    for i in string1:
        if 'A' <= i <= 'Z': 
            count += 1
    print("Number of capital letters:",count)
    print("Thread name is:",threading.current_thread().name)
    print("thread id of Capital is:",threading.get_ident())

def Display_Digits(string1):
    count = 0
    for i in string1:
        if '0' <= i <= '9': 
            count += 1
    print("Number of digits:",count)
    print("Thread name is:",threading.current_thread().name)
    print("thread id of digit is:",threading.get_ident())

def main():
    print("Enter any string")
    str1 = input()

    small = threading.Thread(target=Display_small, args=(str1,))
    capital = threading.Thread(target=Display_capital, args=(str1,))
    digits = threading.Thread(target=Display_Digits, args=(str1,))

    small.start()
    capital.start()
    digits.start()

    small.join()
    capital.join()
    digits.join()

if __name__ == "__main__":
    main()