#Create a function that accepts a number and prints a reverse countdown using a While Loop.

# def runloopFrom(x, y):
#     for i in range(x, y):
#         print(i)

# runloopFrom(-10, 0)  

num = int(input("Enter a number: "))

def reverse_countdown(num):
    while num >= 0:
        print(num)
        num -= 1

reverse_countdown(num)