def is_prime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def main():

    print("Enter a number")

    num = int(input())

    ret = is_prime(num)

    if (ret):
        print(f"{num} is prime number")
    else:
        print(f"{num} is not a prime number")

if __name__ == "__main__":
    main()