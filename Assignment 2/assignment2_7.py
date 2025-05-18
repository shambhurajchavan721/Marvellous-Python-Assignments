def Pattern(No1):
    for i in range(No1):
        for j in range(No1):
            print(j+1," ",end="")
        print("\n")

def main():
    Value = 0
    Value = int(input("Enter Number: "))

    Pattern(Value)

if __name__ == "__main__":
    main()