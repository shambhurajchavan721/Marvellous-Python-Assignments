from functools import reduce

Filter_List = lambda A : 70 <= A <=90

Map_List = lambda A : A + 10

Reduce_List = lambda A , B : A * B

def main():

    print("Enter number of elements in a list")
    Size = int(input())

    Data = []
    print("Enter elements in list")
    for i in range(Size):
        i = int(input())
        Data.append(i)

    print("Input List =",Data)

    FData = list(filter(Filter_List,Data))

    print("List after Filter =",FData)

    MData = list(map(Map_List,FData))

    print("List after Map =",MData)

    RData = reduce(Reduce_List,MData)

    print("Output of reduce",RData)

if __name__ == "__main__":
    main()