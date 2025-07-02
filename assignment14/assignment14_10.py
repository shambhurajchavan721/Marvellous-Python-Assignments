class Employee:
    def _init_(self, name, department, salary):
        self.name = name
        self._department = department
        self.__salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Salary:", self.__salary)

def main():
    emp = Employee("David", "Sales", 45000)
    emp.display_info()
    print("Accessing protected:", emp._department)
    print("Accessing private via name mangling:", emp.Employee_salary)

if __name__ == "__main__":
    main()