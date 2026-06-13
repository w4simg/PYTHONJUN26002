#Create a function that accepts a number and prints its multiplication table up to 10.

num = int(input("Enter a number: "))

def multi_table(num):
    for n in range(1, 11):
        s = num * n
        print("multiplication is=", s)

multi_table(num)