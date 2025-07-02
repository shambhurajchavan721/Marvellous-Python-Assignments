def main():
    with open("marks.txt", "w") as file:
        for i in range(5):
            name = input(f"Enter name of student {i + 1}: ")
            marks = input(f"Enter marks of {name}: ")
            file.write(f"{name} {marks}\n")

    print("\nStudents who scored more than 75 marks:")
    with open("marks.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2 and parts[1].isdigit():
                if int(parts[1]) > 75:
                    print(parts[0])

if __name__ == "__main__":
    main()