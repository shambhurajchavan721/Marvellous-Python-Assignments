import multiprocessing

def factorial(No):
    fact = 1
    while(No>=1):
        fact = fact * No
        No = No -1 
    return fact

def main():

    Data = [4,10,6.8,12,9,34,23,5,18]

    Result = []
    P = multiprocessing.Pool()

    Result = P.map(factorial,Data)

    print(Result)

if __name__ == "__main__":
    main()