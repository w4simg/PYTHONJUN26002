# Print all keys and values separately.

student = {
    "name": "wasim",
    "age": 21,
    "course": "Python",
    "city": "Bhubaneswar",
    "email": "wasim@example.com"
}

print("Dictionary:", student)

# Print keys separately
print("\nKeys:")
for key in student.keys():
    print(key)

# Print values separately
print("\nValues:")
for value in student.values():
    print(value)
