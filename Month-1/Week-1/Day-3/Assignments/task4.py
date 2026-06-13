#Take marks as input and assign grades according to the following criteria.
#Marks      | Grade
# 90+       | A
# 70-89     | B
# 40-69     | C
# Below 40  | Fail

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")