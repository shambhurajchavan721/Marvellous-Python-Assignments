def main():
    print("Enter temperature in celcius:")
    Temp1 = int(input())

    FTemp = float(Temp1 * 1.8 + 32) 

    print("Temperature in Fahrenheit is",FTemp,"F")
    

if __name__ == "__main__":
    main()