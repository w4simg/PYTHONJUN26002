#Create a function that accepts a number and returns the sum of all numbers from 1 to that number.

num = int(input("Enter a number: "))

def sum_numbs(num):
    s = 0
    for i in range(1, num + 1):
        s += i
    return s

result = sum_numbs(num)
print("The sum of all numbers from 1 to", num, "is:", result)