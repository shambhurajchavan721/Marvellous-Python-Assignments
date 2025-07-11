class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b


def main():
    calc = Calculator()

    print("Simple Calculator")
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input.")
        return

    if choice == '1':
        print(f"Result: {calc.add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {calc.subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {calc.multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {calc.divide(num1, num2)}")


if __name__ == "__main__":
    main()