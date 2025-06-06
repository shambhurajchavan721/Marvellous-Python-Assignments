def Factorial(value):
    fact = 1
     
    for i in range (1,value+1):
        fact = fact * i
        
    return fact


def main():

    no= int(input("Enter number the number:"))
    
    
    Ret= Factorial(no)

    print("Factorial of :",Ret)

if  __name__== "__main__":
    main()