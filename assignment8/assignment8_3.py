import threading

def AddEven(Input_List):
    Sum = 0
    for i in Input_List:
        if i % 2 == 0:
            Sum = Sum + i

    print("Addition of even elements is:",Sum)
    

def AddOdd(Input_List):
    Sum = 0
    for i in Input_List:
        if i % 2 != 0:
            Sum = Sum + i

    print("Addition of even elements is:",Sum)


def main():
    print("Enter the number of integer elements")
    Size = int(input())

    Input_List = []
    print("Enter the integer elements")
    for i in range(Size):
        No = int(input())
        Input_List.append(No)

    EvenList = threading.Thread(target= AddEven,args=(Input_List,))
    OddList = threading.Thread(target= AddOdd,args=(Input_List,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

if __name__ == "__main__":
    main()