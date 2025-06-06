def DigitAdd(value):
    add=0
    while (value!=0):
        add =add+value % 10
        value=value//10
        return add
def main():
    no= int(input("Enter Number: "))

    Ans=DigitAdd(no)

    print("Addition of digits is ",Ans)

if __name__ == "__main__":
    main()