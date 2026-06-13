#Create a function that accepts two numbers as parameters and prints the larger number.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
def find_larger(num1, num2):
    if num1 > num2:
        print(num1, "is larger")
    elif num2 > num1:
        print(num2, "is larger")
    else:
        print("Both numbers are equal")

find_larger(num1, num2)

