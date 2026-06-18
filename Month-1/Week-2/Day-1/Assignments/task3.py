# Task 3: Create a Constructor
# Requirements:
# - Create a class named Employee.
# - Use a constructor (__init__).
# - Accept: employee name, employee id, salary.
# - Create 3 employee objects.
# - Display all employee details.

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print(f"ID: {self.emp_id} | Name: {self.name} | Salary: {self.salary}")

# Create 3 employee objects
emp1 = Employee("Alice", "EMP01", 50000)
emp2 = Employee("Bob", "EMP02", 60000)
emp3 = Employee("Charlie", "EMP03", 55000)

# Display all employee details
print("Employee List:")
emp1.display()
emp2.display()
emp3.display()
