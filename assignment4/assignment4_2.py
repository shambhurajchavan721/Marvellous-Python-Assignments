def main():
    multi= lambda A,B: A * B

    no1=int(input("enter first number:"))

    no2=int(input("enter second number:"))
    
    ret=multi(no1,no2)

    print("multiplication is:",ret)
    

if __name__ =="__main__":
    main()