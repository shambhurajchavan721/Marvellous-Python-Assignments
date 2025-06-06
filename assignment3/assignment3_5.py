import MarvellousNum


def listprime(list1):
    sum=0
    for i in list1:
        if MarvellousNum.checkprime(i):
            sum=sum=1
    return sum
        
def main():
    Size = int(input("Enter Number of Elements: "))
    
    data=[]

    print("enter the number")
    for i in range (Size):
        i=int(input())
        data.append(i)

    ret=listprime(data)
    
    print("Addition of all prime numbers is: ",ret)

if __name__ == "__main__":
    main()