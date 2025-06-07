total = 0
def CountZeros(No):
    global total

    if(No>0):
        temp =  No % 10
        if temp == 0:
            total = total + 1
        No = No//10
        CountZeros(No)

        return total

def main():
    print("enter any integer number")

    Num = int(input())

    Ret = CountZeros(Num)

    print("count of zeros is:",Ret)


if __name__ == "__main__":
    main()