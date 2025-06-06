from functools import reduce

def FMR(Data):

    print("Input List =",Data)

    FData = list(filter(lambda No: (No % 2 == 0),Data))

    print("List after Filter =",FData)

    MData = list(map(lambda No : (No ** 2),FData))

    print("List after MAP =",MData)

    Rdata = reduce(lambda A,B : A + B,MData)

    print("Output of reduce =",Rdata)


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