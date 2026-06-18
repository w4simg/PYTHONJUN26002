# Task 11: Create a Teacher Class
# Requirements:
# - Create a class named Teacher.
# - Store: name, subject, experience.
# - Use a constructor.
# - Print teacher information using a method.

class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def print_info(self):
        print("Teacher Profile:")
        print("Name:", self.name)
        print("Subject:", self.subject)
        print("Experience:", self.experience, "years")

# Create object
teacher1 = Teacher("Mrs. Sen", "Mathematics", 12)

# Print info
teacher1.print_info()
