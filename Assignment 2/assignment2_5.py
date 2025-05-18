def CheckPrime(No1):
    Temp = No1 - 1
    Flag = True
    
    while (Temp > 1):
        if ((No1 % Temp) == 0):
            Flag = False
            return Flag
        Temp = Temp - 1

    return Flag

def main():
    Value1 = 0
    Value1 = int(input("Enter Number To Check If It Is Prime or Not: "))

    Ans = False
    Ans = CheckPrime(Value1)

    if Ans == True:
        print(Value1," is a prime number")
    else:
        print(Value1," is not a prime number")
    
if __name__ == "__main__":
    main()