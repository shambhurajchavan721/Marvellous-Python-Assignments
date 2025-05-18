def SumFact(No1):
    Temp1 = No1/2
    Temp2 = 0

    while (Temp1 >= 1):
        if (No1 % Temp1 == 0):
            Temp2 = Temp2 + Temp1
        Temp1 = Temp1 - 1

    return Temp2

def main():
    Value1 = 0
    Value1 = int(input("Enter The Number To Get Sum Of Factors: "))
    
    Ans = 0
    Ans = int(SumFact(Value1))

    print("Factors of ",Value1," are ",Ans)

if __name__ == "__main__":
    main()