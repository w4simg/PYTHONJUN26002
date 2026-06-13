#Create a function that accepts a number as a parameter and checks whether it is even or odd using an if-else statement.
num = int(input("Enter a number: "))

def check_even_odd(num):
    if num % 2 == 0:
        print(num, "even num")
    else:
        print(num, "odd num")

check_even_odd(num)