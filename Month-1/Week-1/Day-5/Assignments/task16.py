# Count the total number of elements in a list without using len().

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple"]
print("List:", fruits)

count = 0
for element in fruits:
    count += 1

print("Total number of elements (calculated manually):", count)
