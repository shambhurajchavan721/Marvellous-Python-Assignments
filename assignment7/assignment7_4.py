from functools import reduce

reduce_list = lambda A,B : A * B 

def main():
    Data = []
    print("enter number of elements")
    size = int(input())
    print("Enter the elements")
    for i in range(size):
        No = int(input())
        Data.append(No)

    Rdata = reduce(reduce_list,Data)

    print("Product:",Rdata)
    


if __name__ == "__main__":
    main()