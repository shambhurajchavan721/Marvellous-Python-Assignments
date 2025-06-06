import assignment2_module

def main():
    no1 = int(input("Enter Number 1: "))
    no2 = int(input("Enter Number 2: "))

    ans = 0

    ans = assignment2_module.Add(no1,no2)
    print("Addition of two numbers is: ",ans)

    ans = assignment2_module.Sub(no1,no2)
    print("Subtraction of two numbers is: ",ans)

    ans = assignment2_module.Mult(no1,no2)
    print("Multiplication of two numbers is: ",ans)

    ans = assignment2_module.Div(no1,no2)
    print("Division of two numbers is: ",ans)
    
if __name__ == "__main__":
    main()