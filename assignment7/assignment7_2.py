Modify = lambda A : A *2

def main():
    Data = []
    print("enter number of elements")
    size = int(input())
    print("Enter the elements")
    for i in range(size):
        No = int(input())
        Data.append(No)

    Mdata = list(map(Modify,Data))

    print("Doubled list",Mdata)
    


if __name__ == "__main__":
    main()