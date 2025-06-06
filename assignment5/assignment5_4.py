def main():

    print("Enter first number")
    No1 = int(input())

    print("Enter second number")
    No2 = int(input())

    print("Enter Third number")
    No3 = int(input())

    if (No1>No2):
        if(No1>No3):
            print("Largest number is",No1)
        else:
            print("Largest number is",No3)
    else:
        if(No2>No3):
            print("Largest number is",No2)
        else:
            print("Largest number is",No3)


if __name__ == "__main__":
    main()