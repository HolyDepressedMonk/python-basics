# Print:

# The student with the highest marks.
# The highest marks.
# The average marks.

# Expected:

# Highest: Charlie
# Marks: 91
# Average: 79.0

students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 68
}

max_key, max_value = max(students.items(), key=lambda x:x[1])
avg_value =sum(students.values()) / len(students)
print(f'Highest: {max_key}\nMarks: {max_value}\nAverage: {avg_value}')