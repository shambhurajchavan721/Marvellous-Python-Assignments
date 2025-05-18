def Pattern(No1):
    for i in range(No1):
        for j in range(No1):
            print("* ",end="")  
        print(" ")

def main():
    Value1 = 0

    Value1 = int(input("Enter The Number: "))

    Pattern(Value1)

if __name__== "__main__":
    main()