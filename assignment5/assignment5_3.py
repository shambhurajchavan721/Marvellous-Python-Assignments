def main():
    print("Enter your age:")
    age = int(input())

    if (age < 18):
        print("Not Eligible to vote")
    else:
        print("Eligible to vote")

if __name__== "__main__":
    main()