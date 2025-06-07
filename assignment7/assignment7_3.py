filter_list = lambda A : A % 2 == 0

def main():
    Data = []
    print("enter number of elements")
    size = int(input())
    print("Enter the elements")
    for i in range(size):
        No = int(input())
        Data.append(No)

    Fdata = list(filter(filter_list,Data))

    print("Even Numbers",Fdata)
    


if __name__ == "__main__":
    main()