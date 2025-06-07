i = 1
def display(N):
    global i
    if i < N+1:
        print(i,end= '\t')
        i = i + 1
        display(N)


def main():
    print("enter any integer")
    
    Num = int(input())

    display(Num)

if __name__ =="__main__":
    main()