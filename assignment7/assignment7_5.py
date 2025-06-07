def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
      
        if s[left] != s[right]:
            return 0

        left += 1
        right -= 1

    return 1

def main():
    print("Enter a string")

    str1 = input()

    ret = is_palindrome(str1)

    if (ret):
        print(f"{str1} is palindrome")

if __name__ == "__main__":
    main()