def DigitAdd(No1):
    Digit = int(0)
    Temp = int(No1)
    Temp2 = 0

    while (Temp != 0):
        Digit = int(Temp % 10)
        Temp2 = Temp2 + Digit
        Temp = int(Temp / 10)

    return Temp2

def main():
    Value = int(input("Enter Number: "))

    Ans = 0
    Ans = DigitAdd(Value)

    print("Addition of digits in ",Value," is ",Ans)

if __name__ == "__main__":
    main()