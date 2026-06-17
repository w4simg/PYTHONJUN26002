# Create two sets:
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# Perform: Union, Intersection, and Difference

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)

# Union
print("Union (A U B):", A.union(B))

# Intersection
print("Intersection (A n B):", A.intersection(B))

# Difference (A - B)
print("Difference (A - B):", A.difference(B))

# Difference (B - A)
print("Difference (B - A):", B.difference(A))
