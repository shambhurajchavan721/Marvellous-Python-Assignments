def is_prime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def main():
    Data = []
    print("enter number of elements")
    size = int(input())
    print("Enter the elements")
    for i in range(size):
        No = int(input())
        Data.append(No)

    Fdata = list(filter(is_prime,Data))

    print("Prime Numbers",Fdata)
    


if __name__ == "__main__":
    main()