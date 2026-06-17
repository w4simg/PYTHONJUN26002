# Mini Student Management System
# A menu-driven program:
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Exit
# Uses Strings, Lists, and Dictionaries.

students = []  # List to store student dictionaries

def add_student():
    print("\n--- Add Student ---")
    name = input("Enter Student Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
        
    try:
        age = int(input("Enter Student Age: "))
    except ValueError:
        print("Invalid age. Age must be a number.")
        return
        
    course = input("Enter Student Course: ").strip()
    city = input("Enter Student City: ").strip()
    
    # Store student details in a dictionary
    student = {
        "name": name,
        "age": age,
        "course": course,
        "city": city
    }
    
    students.append(student)
    print(f"Student '{name}' added successfully!")

def view_students():
    print("\n--- View Students ---")
    if not students:
        print("No student records available.")
        return
        
    print(f"{'No.':<4}{'Name':<15}{'Age':<6}{'Course':<15}{'City':<15}")
    print("-" * 55)
    for idx, student in enumerate(students, 1):
        print(f"{idx:<4}{student['name']:<15}{student['age']:<6}{student['course']:<15}{student['city']:<15}")

def search_student():
    print("\n--- Search Student ---")
    if not students:
        print("No student records available to search.")
        return
        
    search_name = input("Enter student name to search: ").strip().lower()
    found = False
    
    for student in students:
        if student["name"].lower() == search_name:
            print("\nStudent Found:")
            print(f"  Name:   {student['name']}")
            print(f"  Age:    {student['age']}")
            print(f"  Course: {student['course']}")
            print(f"  City:   {student['city']}")
            found = True
            break
            
    if not found:
        print(f"No student found with the name '{search_name}'.")

def main():
    while True:
        print("\n===============================")
        print("   STUDENT MANAGEMENT SYSTEM   ")
        print("===============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")
        print("===============================")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
