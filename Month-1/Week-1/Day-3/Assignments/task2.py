#Take a person's age as input and check whether they are eligible to vote.
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print("you are eligible to vote.")
else:
    print("you are not eligible to vote.")

