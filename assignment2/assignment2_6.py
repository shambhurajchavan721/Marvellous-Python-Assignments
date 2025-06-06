def Pattern(value):
    for i in range(value,0,-1):
       for j in range(i):
           print("*",end="\t")
       print()
def main():
    no=int(input("enter the number:"))

    Pattern(no)

if __name__ == "__main__":
    main()