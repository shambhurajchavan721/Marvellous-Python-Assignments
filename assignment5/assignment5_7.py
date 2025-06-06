def Display(Len,Width):

    print("Area:",Len * Width)

    print("Perimeter:",2 *(Len + Width))

def main():
    print("Enter length of rectangle:")
    Len = int(input())

    print("Enter width of rectangle:")
    Width = int(input())

    Display(Len,Width)

if __name__ == "__main__":
    main()