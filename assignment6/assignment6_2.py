def main():
    SumEven = 0
    for i in range(101):
        if (i % 2 == 0):
            SumEven = SumEven + i
    
    print("Sum of even numbers between 1 to 100 is:",SumEven)



if __name__ == "__main__":
    main()