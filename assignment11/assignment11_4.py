power = 1
def CountPower(No,pow):
    global power

    if(pow>0):
        power = power * No
        pow = pow -1
        CountPower(No,pow)

    return power

def main():
    print("enter any integer number ")

    Num = int(input())

    print("Enter the number to count power")

    Num2 = int(input())

    Ret = CountPower(Num,Num2)

    print(f"power ({Num},{Num2}):",Ret)



if __name__ == "__main__":
    main()