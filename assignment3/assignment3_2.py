def checkmaximum(list1):
   max_value=list1[0]
   for i in list1:
       if i > max_value:
           max_value=i
   return max_value
def main():
    size=int(input("enter number of elements"))
    data=[]
    print("enter the numbers")
    for i in range (size):
        i=int (input())
        data.append(i)
    ret=checkmaximum(data)
    print("maximum number in the list is: ",ret)

if __name__ == "__main__":
    main()