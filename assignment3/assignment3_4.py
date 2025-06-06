def CheckFreq(List1,value):

    Count = 0

    for i in  List1:
        if (i==value):
            Count = Count + 1

    return Count
    

def main():
    
    Size = int(input("Enter Number of Elements: "))
    data=[  ]

    print("enter the numbers")
    for i in range (Size):
        i = int(input())
        data.append(i)
    
    print("enter the number to search frequency ")
    no=int(input())

    ret= CheckFreq(data,no)

    print("Frequency of no is ",ret)
    
if __name__ == "__main__":
    main()