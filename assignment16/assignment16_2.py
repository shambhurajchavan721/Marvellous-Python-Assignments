def main():
    try:
        with open("data.txt", "r") as file:
            content = file.read()
            print("Contents of data.txt:\n")
            print(content)
    except FileNotFoundError:
        print("Error: The file 'data.txt' does not exist.")

if __name__ == "__main__":
    main()