def Pattern(No1):
    Temp = 1

    while (Temp <= No1):
        for i in range (Temp):
            print(i+1, " ", end=" ")
        print("\n")
        Temp = Temp + 1

def main():
    Value = 0
    Value = int(input("Enter the number: "))

    Pattern(Value)

if __name__ == "__main__":
    main()