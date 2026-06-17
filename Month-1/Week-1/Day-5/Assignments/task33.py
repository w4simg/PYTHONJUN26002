# Take a string input and remove duplicate characters while preserving the original order.
# Example Input: "programming" -> Output: "progamin"

user_input = input("Enter a string: ")

seen = set()
unique_chars = []

for char in user_input:
    if char not in seen:
        seen.add(char)
        unique_chars.append(char)

result = "".join(unique_chars)
print("String after removing duplicate characters:", result)
