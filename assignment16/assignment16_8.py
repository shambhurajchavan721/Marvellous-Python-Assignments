def main():
    with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
        for line in infile:
            if line.strip():
                outfile.write(line)

if __name__ == "__main__":
    main()