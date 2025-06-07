from functools import reduce

def is_prime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def FMR(Data):
    print("Input List =", Data)

    FData = list(filter(is_prime, Data))
    print("List after Filter  =", FData)

    MData = list(map(lambda No: No * 2, FData))
    print("List after Map =", MData)

    if MData:
        Rdata = reduce(lambda A, B: A if A > B else B, MData)
    else:
        Rdata = None
    print("Output of reduce =", Rdata)

def main():
    List1 = []
    print("Enter number of elements")
    size = int(input())
    print("Enter the numbers")
    for i in range(size):
        i = int(input())
        List1.append(i)

    FMR(List1)

if __name__ == "__main__":
    main()