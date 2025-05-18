def Pattern(No1):
    Temp = No1

    for i in range (No1):
        for j in range (Temp):
            print("* ",end="")
        Temp = Temp - 1
        print("\n")

def main():
    Value = 0
    Value = int(input("Enter Number: "))

    Pattern(Value)

if __name__ == "__main__":
    main()