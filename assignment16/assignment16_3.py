def main():
    try:
        with open("data.txt", "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            char_count = sum(len(line) for line in lines)

            print("Lines:", line_count)
            print("Words:", word_count)
            print("Characters:", char_count)
    except FileNotFoundError:
        print("Error: The file 'data.txt' does not exist.")

if __name__ == "__main__":
    main()