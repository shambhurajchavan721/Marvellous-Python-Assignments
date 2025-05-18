def Fact(No1):
    Temp = No1
    Ans = 1

    while (Temp >= 1):
        Ans = Ans * Temp
        Temp = Temp - 1

    return Ans


def main():
    Value1 = 0
    Value1 = int(input("Enter number to get factorial: "))
    
    Ret1 = 0
    Ret1 = Fact(Value1)

    print("Factorial of ",Value1," is ",Ret1)

if  __name__== "__main__":
    main()