def add(no1,no2):
    res=0
    res=no1+no2
    return res
def main():
    value1=int(input("enter first no:"))
    value2=int(input("enter second no:"))

    ans=add(value1,value2)
    print("addition of two numbers is:",ans)
if __name__ =="__main__":
    main()