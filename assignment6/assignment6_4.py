def main():
    print("Enter a number")
    num = int(input())
    fact = 1
    for i in range(num,1,-1):
        fact = fact * i
    
    print(f"factorial of {num} is",fact)

if __name__ == "__main__":
    main()