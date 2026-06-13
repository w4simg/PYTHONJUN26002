'''Description:  Create a function that accepts username and password as parameters.

Conditions:
*Username = admin
*Password = 1234
*Use Nested If.

# Output:
>Login Successful
 or
>Wrong Password
 or
>Invalid User'''

username = input("Enter username: ")
password = input("Enter password: ")

def login(username, password):
    if username == "admin":
        if password == "1234":
            print("Login Successful")
        else:
            print("Wrong Password")
    else:
        print("Invalid User")

login(username, password)  