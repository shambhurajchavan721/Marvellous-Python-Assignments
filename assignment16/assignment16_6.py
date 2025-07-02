def main():
    try:
        with open("source.txt", "r") as source, open("destination.txt", "w") as destination:
            for line in source:
                destination.write(line)
        print("Contents copied successfully.")
    except FileNotFoundError:
        print("Error: The file 'source.txt' does not exist.")

if __name__ == "__main__":
    main()