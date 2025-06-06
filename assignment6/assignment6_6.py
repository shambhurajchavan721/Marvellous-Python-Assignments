def Display(No):
    for i in range(1,No+1):
        for j in range(i):
            print("*",end=" ")
        print()

def main():  
    Display(4)

if __name__ == "__main__":
    main()