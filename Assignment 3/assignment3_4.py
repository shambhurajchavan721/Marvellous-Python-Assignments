def CheckFreq(DemoList, Size, No1):

    Countr = 0

    for i in range (Size):
        if (DemoList[i] == No1):
            Countr = Countr + 1

    return Countr
    

def main():
    NumLis = []
    Size = 0
    TempNum = 0
    Ans = 0

    Size = int(input("Enter Number of Elements: "))

    for i in range (Size):
        TempNum = int(input("Enter Number: "))
        NumLis.append(TempNum)

    TempNum = int(input("Enter Number To Check Frequency: "))

    Ans = CheckFreq(NumLis, Size, TempNum)

    print("Frequency of ",TempNum," is ",Ans)
    
if __name__ == "__main__":
    main()