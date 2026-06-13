#Create a function that accepts a list of numbers and counts how many numbers are positive.

def positive_numbers(numbers):
    count = 0
    for z in numbers:
        if z > 0:
            count += 1
    return count

numbers = [1, -2, 3, 4, -5, 6]
result = positive_numbers(numbers)  
print("The count of positive numbers is:", result)  