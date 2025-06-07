import threading

def AddEvenFact(No):
    Sum = 0
    for i in range(2,No+1,2):
        if(No % i)== 0:
            Sum = Sum + i
    
    print("Addition of EvenFactor is:",Sum)

def AddOddFact(No):
    Sum = 0
    for i in range(1,No+1,2):
        if(No % i)== 0:
            Sum = Sum + i
    
    print("Addition of odd Factor is:",Sum)

def main():
    
    print("Enter any Integer Number")
    Num = int(input())

    evenfactor = threading.Thread(target=AddEvenFact,args=(Num,))
    oddfactor = threading.Thread(target=AddOddFact,args=(Num,))

    evenfactor.start()
    oddfactor.start()

    evenfactor.join()
    oddfactor.join()
    print("Exit from main")

if __name__ == "__main__":
    main()