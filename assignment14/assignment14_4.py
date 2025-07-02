class Student:
    school_name = "Poddar International School"

    def _init_(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, School: {Student.school_name}")

def main():
    s1 = Student("Rohit", 1)
    s2 = Student("Karan", 2)
    s1.display()
    s2.display()
    Student.school_name = "New English School"
    s1.display()
    s2.display()

if __name__ == "__main__":
    main()