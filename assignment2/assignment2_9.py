def NumLen(value):
    res = str(value)
    Ans = len(res)
    
    return Ans

def main():
    
    no = int(input("Enter Number: "))

    
    Ans = NumLen(no)

    print("Length of number is: ",Ans)

if __name__ == "__main__":
    main()