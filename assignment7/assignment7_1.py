square = lambda A : A ** 2
cube = lambda A : A**3

def main():
    print("enter a number")

    Num = int(input())

    print("square:",square(Num))
    print("Cube:",cube(Num))

if __name__ == "__main__":
    main()