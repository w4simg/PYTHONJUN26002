# Use a loop to print the dictionary items in the format "key : value".

student = {
    "name": "John",
    "age": 22,
    "course": "Python"
}

# Looping and printing in the required format
for key, value in student.items():
    print(f"{key} :{value}")
