# Print all even numbers from the following list:
# numbers = [10, 15, 20, 25, 30, 35, 40]

numbers = [10, 15, 20, 25, 30, 35, 40]
print("Original list:", numbers)

print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)
