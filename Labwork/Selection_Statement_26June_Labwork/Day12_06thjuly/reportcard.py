# Student Subject Report Card

students = {}

# Input details of 3 students
for i in range(3):
    name = input("Enter Student Name: ")

    math = int(input("Enter Math Marks: "))
    science = int(input("Enter Science Marks: "))
    english = int(input("Enter English Marks: "))

    students[name] = {
        "Math": math,
        "Science": science,
        "English": english
    }

# Display Total and Average
print("\nStudent Report Card")

topper = ""
highest_total = 0

for name in students:
    total = students[name]["Math"] + students[name]["Science"] + students[name]["English"]
    average = total / 3

    print("\nStudent:", name)
    print("Total Marks =", total)
    print("Average Marks =", average)

    if total > highest_total:
        highest_total = total
        topper = name

# Display Topper
print("\nTopper:")
print(topper, "with", highest_total, "marks")

# Subject-wise Highest Marks
subjects = ["Math", "Science", "English"]

print("\nSubject-wise Highest Marks:")

for subject in subjects:
    highest = 0
    student_name = ""

    for name in students:
        if students[name][subject] > highest:
            highest = students[name][subject]
            student_name = name

    print(subject, ":", highest, "-", student_name)

# Students with Average >= 85
print("\nStudents with Average >= 85")

found = False

for name in students:
    total = students[name]["Math"] + students[name]["Science"] + students[name]["English"]
    average = total / 3

    if average >= 85:
        print(name, "Average =", average)
        found = True

if found == False:
    print("No student found.")


#output:
'''
    Enter Student Name: harsh
Enter Math Marks: 88
Enter Science Marks: 99
Enter English Marks: 77
Enter Student Name: ankesh
Enter Math Marks: 99
Enter Science Marks: 88
Enter English Marks: 66
Enter Student Name: diksha
Enter Math Marks: 88
Enter Science Marks: 77
Enter English Marks: 66

Student Report Card

Student: harsh
Total Marks = 264
Average Marks = 88.0

Student: ankesh
Total Marks = 253
Average Marks = 84.33333333333333

Student: diksha
Total Marks = 231
Average Marks = 77.0

Topper:
harsh with 264 marks

Subject-wise Highest Marks:
Math : 99 - ankesh
Science : 99 - harsh
English : 77 - harsh

Students with Average >= 85
harsh Average = 88.0
'''