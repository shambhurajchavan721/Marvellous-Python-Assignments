def Pattern(value):
    for i in range(1,value+1):
        for j in range(1,value+1):
            print(j,end="\t")
        print()

def main():
    
    no = int(input("Enter Number: "))

    Pattern(no)

if __name__ == "__main__":
    main()