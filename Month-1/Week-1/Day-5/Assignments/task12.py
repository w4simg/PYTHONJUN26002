# Find the largest number from a list.

numbers = [45, 12, 89, 34, 67, 98, 23]
print("List of numbers:", numbers)

# Method 1: Using built-in max() function
largest_number = max(numbers)
print("Largest number (using max()):", largest_number)

# Method 2: Manual traversal
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number (manual loop):", largest)
