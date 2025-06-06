def main():

    print("Enter a character")
    char1 = input()

    if char1 in "aeiouAEIOU":
        print("char1 is vowel")
    else:
        print("{char1} is a consonent")        




if __name__ == "__main__":
    main()