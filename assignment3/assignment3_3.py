def checkminimum(list1):
   min_value=list1[0]
   for i in list1:
       if i < min_value:
           min_value=i
   return min_value
def main():
    size=int(input("enter number of elements"))
    data=[]
    print("enter the numbers")
    for i in range (size):
        i=int (input())
        data.append(i)
    ret=checkminimum(data)
    print("minimum number in the list is: ",ret)

if __name__ == "__main__":
    main()