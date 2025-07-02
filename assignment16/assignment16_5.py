def main():
    try:
        with open("data.txt", "r") as file:
            for line in file:
                if len(line.split()) > 5:
                    print(line.strip())
    except FileNotFoundError:
        print("Error: The file 'data.txt' does not exist.")

if __name__ == "__main__":
    main()