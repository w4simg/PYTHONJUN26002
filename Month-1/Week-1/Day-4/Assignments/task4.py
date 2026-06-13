#Create a function that accepts age as a parameter and checks whether the person is eligible to vote.

age = int(input("Enter your age: "))

def vote_eligibility(age):
    if age >= 18:
        print("eligible to vote.")
    else:
        print("not eligible to vote.")

vote_eligibility(age)