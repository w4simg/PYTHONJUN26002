
import os

def cls():
    os.system("cls")

name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))
experience = int(input("Enter years of experience: "))

def employee_bonus(name, salary, experience):
    if experience >= 5 and salary < 50000:
        bonus = salary * 0.20
    elif experience >= 3:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05

    final_salary = salary + bonus

    cls()

    print("Employee Name:", name)
    print("Salary:", salary)
    print("Bonus Amount:", bonus)
    print("Final Salary:", final_salary)

employee_bonus(name, salary, experience)