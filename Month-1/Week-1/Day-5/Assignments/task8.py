# Check whether a string is a palindrome or not.

user_input = input("Enter a string: ")
# Remove spaces and normalize casing to make it a robust check
cleaned_input = user_input.replace(" ", "").lower()
reversed_input = cleaned_input[::-1]

if cleaned_input == reversed_input:
    print(f"'{user_input}' is a Palindrome")
else:
    print(f"'{user_input}' is not a Palindrome")
