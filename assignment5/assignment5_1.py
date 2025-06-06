def Display(Value1,Value2):
    
    print("Sum:",Value1 + Value2)

    print("Difference:",Value1 - Value2)

    print("Product:",Value1 * Value2)

    print("Division:",Value1 / Value2)

def main():

    print("Enter first number")
    No1 = int(input())

    print("Enter second number")
    No2 = int(input())

    Display(No1,No2)



if __name__ == "__main__":
    main()