total = 0
def SumOfDigits(No):
    global total

    if(No>0):
        total = total + No % 10
        No = No//10
        SumOfDigits(No)

    return total

def main():
    print("enter any integer number")

    Num = int(input())

    Ret = SumOfDigits(Num)

    print("sum of digits is:",Ret)



if __name__ == "__main__":
    main()