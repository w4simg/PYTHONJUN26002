#Create a function that accepts a number and prints all numbers from 1 to that number using a For Loop.

num = int(input("Enter a number: "))

def print_numbs(num):
    s = num + 1
    for i in range(1, s):
        print(i)

print_numbs(num)