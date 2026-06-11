#task20
#Take a Boolean value from the user and print its opposite using the not operator.

value = input("Enter a Boolean value (True/False): ")

if value == "True":
    print("The opposite is False.")
elif value == "False":
    print("The opposite is True.")
else:
    print("Invalid input. Please enter True or False.")