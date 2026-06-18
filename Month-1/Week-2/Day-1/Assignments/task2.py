# Task 2: Create a Student Class
# Requirements:
# - Create a class named Student.
# - Add attributes: name, age, course.
# - Create a method called displayStudent().
# - Print all student details using the method.

class Student:
    name = ""
    age = 0
    course = ""

    def displayStudent(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

# Create object
student1 = Student()
student1.name = "Rahul"
student1.age = 20
student1.course = "Python Programming"

# Print details using the method
student1.displayStudent()
