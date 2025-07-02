def main():
    students = ["Rohit", "Sanket", "Tushar", "Sneh", "Harshad"]
    with open("student.txt", "w") as file:
        for name in students:
            file.write(name + "\n")

if __name__ == "__main__":
    main()