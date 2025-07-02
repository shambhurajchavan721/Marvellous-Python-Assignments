class Employee:
    def _init_(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")

def main():
    emp = Employee("Rohit", 101, 50000)
    emp.display()

if __name__ == "__main__":
    main()