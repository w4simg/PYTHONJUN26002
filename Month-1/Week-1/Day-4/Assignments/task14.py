#Create a function that accepts a number and prints all odd numbers from 1 to that number.

num = int(input("Enter a number: "))

def odd_numbs(num):
    s = num + 1
    for z in range(1, s):
        if z % 2 != 0:
            print(z)
        else:
            print(z, "is even num")

odd_numbs(num)