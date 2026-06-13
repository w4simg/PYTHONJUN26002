marks = int(input("Enter marks: "))
income = int(input("Enter family income: "))

if marks >= 85:
    if income < 500000:
        print("Scholarship Approved")
    else:
        print("Scholarship Rejected")
else:
    print("Scholarship Rejected")