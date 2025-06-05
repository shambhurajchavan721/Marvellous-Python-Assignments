def chknum(no):
   if (no%2==0):
    print("even number")
   else:
    print("odd number")

def main():
    print("enter the number")
    value=int(input())
    chknum(value)

if __name__ == "__main__":
    main()