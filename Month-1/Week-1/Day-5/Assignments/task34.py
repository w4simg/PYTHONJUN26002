# Convert two lists (keys and values) into a dictionary.
# keys = ["name", "age", "city"]
# values = ["John", 22, "Mumbai"]

keys = ["name", "age", "city"]
values = ["John", 22, "Mumbai"]

print("Keys list:", keys)
print("Values list:", values)

# Method 1: Using zip()
result_dict = dict(zip(keys, values))
print("\nConverted Dictionary (using zip):", result_dict)

# Method 2: Using manual loop for demonstration
manual_dict = {}
for i in range(len(keys)):
    manual_dict[keys[i]] = values[i]
print("Converted Dictionary (using loop):", manual_dict)
