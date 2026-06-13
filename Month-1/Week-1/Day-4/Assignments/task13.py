#o
marks = int(input("Enter your marks: "))

def calculate_grade(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 70:
        print("Grade B")
    elif marks >= 40:
        print("Grade C")
    else:
        print("Fail")

calculate_grade(marks)