# Calculate the sum of all numbers in a list.

numbers = [10, 20, 30, 40, 50]
print("List of numbers:", numbers)

# Method 1: Using built-in sum() function
total_sum = sum(numbers)
print("Sum (using sum()):", total_sum)

# Method 2: Manual sum with a loop
manual_sum = 0
for num in numbers:
    manual_sum += num
print("Sum (manual loop):", manual_sum)
