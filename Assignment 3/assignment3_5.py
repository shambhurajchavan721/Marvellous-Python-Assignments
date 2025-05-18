from MarvellousNum import CheckPrime
from MarvellousNum import AddPrime

def main():
    NumLis = []
    Size = 0
    TempNum = 0
    Ans1 = []
    Ans2 = 0

    Size = int(input("Enter Number of Elements: "))

    for i in range (Size):
        TempNum = int(input("Enter Number: "))
        NumLis.append(TempNum)

    Ans1 = CheckPrime(NumLis, Size)

    Ans2 = AddPrime(Ans1)

    print("Addition of all prime numbers is: ",Ans2)

if __name__ == "__main__":
    main()