i =1
j =1
def Display(row):
    global i, j

    if i <= row:
        if j <= i:
            print("*", end="\t")
            j = j + 1
            Display(row)
        else:
            print()
            i = i + 1
            j = 1
            Display(row)

def main():
    print("enter no of rows")

    row = int(input())

    Display(row)

if __name__ == "__main__":
    main()