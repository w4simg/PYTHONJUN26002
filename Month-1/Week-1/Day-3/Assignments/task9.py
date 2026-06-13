#Take a number as input and print its multiplication table from 1 to 10.

num = int(input("Enter a number: "))

for z in range(1, 11):
    s = num * z
    print(num, "x", z, "=", num * z)