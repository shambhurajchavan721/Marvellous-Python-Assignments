total = 0
def Sum_N(No):
    global total

    if(No>0):
        total = total + No
        No = No - 1
        Sum_N(No)

        return total

def main():
    print("enter any integer number")

    Num = int(input())

    Ret = Sum_N(Num)

    print(f"Sum of numbers till {Num} is:",Ret)


if __name__== "__main__":
    main()