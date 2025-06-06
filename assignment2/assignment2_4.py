def SumFact(value):
    add=0
    for i in range (1,value):
        if(value % i == 0):
            add =add + i
        return add
def main():
    
    no= int(input("Enter The Number To Get Sum Of Factors: "))
    
    ret=SumFact(no)
    print("Factors of :",ret)

if __name__ == "__main__":
    main()