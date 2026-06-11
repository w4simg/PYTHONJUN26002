#task14
#Take age and citizenship status from the user and check whether the person is eligible to vote.

age = int(input("Enter your age: "))
citizenship = input("Are you an Indian? (yes/no): ")

if age >= 18 and citizenship == "yes":
    print("eligiable")
else:
    print("not eligible")