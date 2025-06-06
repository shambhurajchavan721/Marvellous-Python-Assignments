def Addition(list1):
    
    Addition =0
    for i in list1:
        Addition=Addition+i
    return Addition

def main():
    size=int(input("enter number of elements"))
    data=[]
    print("enter the numbers")
    for i in range (size):
        i=int (input())
        data.append(i)
    ret=Addition(data)
    print("Addition of All Elements Is: ",ret)

if __name__ == "__main__":
    main()