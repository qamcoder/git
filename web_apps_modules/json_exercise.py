import json

# Read JSON file
with open("students.json", 'r') as json_data:
    students = json.load(json_data)


# Calculate average grade
total_grade = sum([student["grade"] for student in students])
average_grade = total_grade / len(students)


# Print names of students above average grade
for student in students:
    if student["grade"] >= average_grade:
        print(student["name"])
