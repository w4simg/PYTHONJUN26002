# Find the smallest number from a list.

numbers = [45, 12, 89, 34, 67, 98, 23]
print("List of numbers:", numbers)

# Method 1: Using built-in min() function
smallest_number = min(numbers)
print("Smallest number (using min()):", smallest_number)

# Method 2: Manual traversal
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest number (manual loop):", smallest)
