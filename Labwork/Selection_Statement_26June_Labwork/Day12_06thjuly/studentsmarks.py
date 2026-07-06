
# Student Marks Management

students = {}

# Input marks of 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Display all students
print("\nStudent Names and Marks:")
for name in students:
    print(name, ":", students[name])

# Add a new student
name = input("\nEnter new student name: ")
marks = int(input("Enter marks: "))
students[name] = marks

print("\nAfter Adding Student:")
for name in students:
    print(name, ":", students[name])

# Update marks of an existing student
name = input("\nEnter student name to update marks: ")

if name in students:
    marks = int(input("Enter new marks: "))
    students[name] = marks
    print("Marks Updated Successfully.")
else:
    print("Student not found.")

print("\nAfter Updating Marks:")
for name in students:
    print(name, ":", students[name])

# Delete a student
name = input("\nEnter student name to delete: ")

if name in students:
    del students[name]
    print("Student Deleted Successfully.")
else:
    print("Student not found.")

print("\nAfter Deleting Student:")
for name in students:
    print(name, ":", students[name])

# Display student with highest marks
highest_student = ""
highest_marks = -1

for name in students:
    if students[name] > highest_marks:
        highest_marks = students[name]
        highest_student = name

print("\nStudent with Highest Marks:")
print(highest_student, ":", highest_marks)

#output:
'''
Enter student name: harsh sharma
Enter marks: 99
Enter student name: ankesh 
Enter marks: 90
Enter student name: diksha
Enter marks: 45
Enter student name: aadarsh
Enter marks: 87
Enter student name: vardhan
Enter marks: 88

Student Names and Marks:
harsh sharma : 99
ankesh  : 90
diksha : 45
aadarsh : 87
vardhan : 88

Enter new student name: kanishak
Enter marks: 88

After Adding Student:
harsh sharma : 99
ankesh  : 90
diksha : 45
aadarsh : 87
vardhan : 88
kanishak : 88

Enter student name to update marks: kanishak
Enter new marks: 87
Marks Updated Successfully.

After Updating Marks:
harsh sharma : 99
ankesh  : 90
diksha : 45
aadarsh : 87
vardhan : 88
kanishak : 87

Enter student name to delete: harsh sharma
Student Deleted Successfully.

After Deleting Student:
ankesh  : 90
diksha : 45
aadarsh : 87
vardhan : 88
kanishak : 87

Student with Highest Marks:
ankesh  : 90
'''