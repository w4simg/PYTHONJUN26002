# def myfrstfunct():
#     print("Hello World")

# myfrstfunct()

# def addTwonum():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))

#     print("The sum is:", a + b)

# addTwonum()

# def mysecondfunct(para,  para2):
#     print( para, para2)

# mysecondfunct("Hello", "World")

# def addTwonum(a, b):
#     print("The sum is:", a + b)

# addTwonum(5, 5)

# def runloopFrom(x, y):
#     for i in range(x, y):
#         print(i)

# runloopFrom(1, 11)
# runloopFrom(-10, 0)  

# def zzz():
#     return "Hello World"
# print(zzz())

# def studentdetails():
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     per = int(input("Enter your per: "))
#     reg = (input("Enter your reg: "))

#     print( name, age, per, reg)

# studentdetails()


# name = "sst"

# def localfunction():
#         name_1 = "sstech"
# print(name, name_1)
    
# print(name)

# localfunction()

#make a functions that takes color  as parameter and return the result 
# in color options red-stop, green-go, orange-start

def colors(options):
    if options == "red":
        return 'stop'
    elif options == "green":
        return 'go'
    elif options == "orange":
        return 'start'
    else:
        print("check again")

options = input("Enter the color: ")
print(colors(options))