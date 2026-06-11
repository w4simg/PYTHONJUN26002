#task15
#Take student status and premium membership status from the user and check whether the user is eligible for a discount.

student = input("student? (y/n): ")
premium = input("premium membership? (y/n): ")

if student == "y" or premium == "y":
    print("eligible for discount.")
else:
    print("not eligible for discount.")