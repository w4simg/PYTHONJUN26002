#task17
#Take marks and sports quota status from the user and check whether the student is eligible for a scholarship.

marks = int(input("Enter your marks: "))
sports_quota = input("sports quota? (y/n): ")

if marks >= 75 or sports_quota == "y":
    print("eligible for scholarship.")
else:
    print("not eligible for scholarship.")