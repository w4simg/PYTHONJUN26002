# Create a dictionary for an employee containing employee_id, employee_name, salary, department
# Display all details in a formatted way.

employee = {
    "employee_id": "EMP1042",
    "employee_name": "Sarah Connor",
    "salary": 75000.0,
    "department": "Cyber Security"
}

print("=========================================")
print("           EMPLOYEE PROFILE              ")
print("=========================================")
print(f" ID:          {employee['employee_id']}")
print(f" Name:        {employee['employee_name']}")
print(f" Salary:      ${employee['salary']:,.2f}")
print(f" Department:  {employee['department']}")
print("=========================================")
