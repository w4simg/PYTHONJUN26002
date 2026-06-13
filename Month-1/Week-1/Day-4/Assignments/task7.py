#Create a function that accepts a number and prints all even numbers from 1 to that number.

num = int(input("Enter a number: "))

def print_even_numbs(num):
    s = num + 1
    for z in range(1, s):
        if z % 2 == 0:
            print(z)
        else:
            print(z, "is odd num")

print_even_numbs(num)