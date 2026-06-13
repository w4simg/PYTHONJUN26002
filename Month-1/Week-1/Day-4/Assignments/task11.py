#Create a function that accepts a number and returns its square.

num = int(input("Enter a number: "))

def square(num):
    s = num ** 2
    return s


ans = square(num)
print("The square of", num, "is:", ans)