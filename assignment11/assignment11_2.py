fact = 1
def factorial(no): 
    global fact
    
    if(no >=1):
        fact = fact * no
        no = no - 1
        factorial(no)

    return fact 

def main():
    print("enter any integer") 
    Num = int(input())

    ret = factorial(Num)

    print(ret)

if __name__ == "__main__":
    main()