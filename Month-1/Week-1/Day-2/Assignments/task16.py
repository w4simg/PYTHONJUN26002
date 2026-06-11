#task16
#Take experience and performance rating from the user and check whether the employee is eligible for a bonus.

experience = int(input("Enter years of experience: "))
rating = int(input("Enter performance rating (1-10): "))

if experience >= 4 and rating >= 7:
    print("eligible for bonus.")
else:
    print("not eligible for bonus.")