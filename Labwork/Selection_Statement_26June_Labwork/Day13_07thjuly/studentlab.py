#wap to calculate the grade of student.
# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"


# Main Program
for i in range(1, 6):
    # Accept marks from the user
    marks = int(input(f"Enter marks of Student {i}: "))

    # Call the function
    grade = calculate_grade(marks)

    # Display result
    print("Marks:", marks)
    print("Grade:", grade)



#output:
'''
    Enter marks of Student 1: 44
Marks: 44
Grade: C
Enter marks of Student 2: 88
Marks: 88
Grade: A
Enter marks of Student 3: 77
Marks: 77
Grade: A
Enter marks of Student 4: 23
Marks: 23
Grade: Fail
Enter marks of Student 5: 5
Marks: 5
Grade: Fail
'''