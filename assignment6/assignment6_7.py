def main():
    Data = []
    print("enter five numbers")
    for i in range(5):
        No = int(input())
        Data.append(No)
    
    Max_Num = Data[0]
    for i in Data:
        if i > Max_Num:
            Max_Num = i
    
    print("Maximum number is",Max_Num)
if __name__ == "__main__":
    main()