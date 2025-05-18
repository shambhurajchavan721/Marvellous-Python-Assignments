def Min(DemoList, Size):
    Temp = DemoList[1]

    for i in range (Size):
        if (DemoList[i] < Temp):
            Temp = DemoList[i]

    return Temp
    

def main():
    NumLis = []
    Size = 0
    TempNum = 0
    Ans = 0

    Size = int(input("Enter Number of Elements: "))

    for i in range (Size):
        TempNum = int(input("Enter Number: "))
        NumLis.append(TempNum)

    Ans = Min(NumLis, Size)

    print("Minimum Number Is: ",Ans)

if __name__ == "__main__":
    main()