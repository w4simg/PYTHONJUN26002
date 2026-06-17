# Create a dictionary of marks, and calculate total and average marks.
# Marks: {"Math": 85, "Science": 90, "English": 78}

marks = {
    "Math": 85,
    "Science": 90,
    "English": 78
}

print("Marks dictionary:", marks)

# Calculate total marks
total_marks = sum(marks.values())

# Calculate average marks
average_marks = total_marks / len(marks)

print("Total Marks:", total_marks)
print("Average Marks:", round(average_marks, 2))
