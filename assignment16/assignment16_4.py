def main():
    with open("numbers.txt", "w") as file:
        for i in range(10):
            num = input(f"Enter number {i + 1}: ")
            file.write(num + "\n")

if __name__ == "__main__":
    main()