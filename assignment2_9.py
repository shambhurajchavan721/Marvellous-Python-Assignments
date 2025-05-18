def NumLen(No1):
    AnsStr = str(No1)
    Ans = len(AnsStr)
    
    return Ans

def main():
    Value = 0
    Value = int(input("Enter Number: "))

    Ans = 0
    Ans = NumLen(Value)

    print("Length of number is: ",Ans)

if __name__ == "__main__":
    main()