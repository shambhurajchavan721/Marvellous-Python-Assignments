def Add(DemoList, Size):
    
    TempAdd = 0
    for i in range (Size):
        TempAdd = TempAdd + DemoList[i]

    return TempAdd

def main():
    NumLis = []
    Size = 0
    TempNum = 0
    Ans = 0

    Size = int(input("Enter Number of Elements You Want To Add: "))

    for i in range (Size):
        TempNum = int(input("Enter Number: "))
        NumLis.append(TempNum)

    Ans = Add(NumLis, Size)

    print("Addition of All Elements Is: ",Ans)

if __name__ == "__main__":
    main()