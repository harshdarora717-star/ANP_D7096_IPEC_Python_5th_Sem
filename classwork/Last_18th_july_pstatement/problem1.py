#Problem 1: Student Management System 
class Student:
    def _init_(self):
        self.student_id = 0
        self.name = ""
        self.course = ""
        self.marks = 0

    def accept_data(self):
        self.student_id = int(input("Enter Student ID : "))
        self.name = input("Enter Name : ")
        self.course = input("Enter Course : ")
        self.marks = int(input("Enter Marks : "))

    def check_result(self):
        if self.marks >= 35:
            return "Pass"
        else:
            return "Fail"

    def display_data(self):
        print("\n------ Student Details ------")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Course     :", self.course)
        print("Marks      :", self.marks)
        print("Result     :", self.check_result())


# Creating object of Student class
student1 = Student()

# Calling methods
student1.accept_data()
student1.display_data()





#output:
'''
Enter Student ID : 101
Enter Name : YASH
Enter Course : BTECH
Enter Marks : 99

------ Student Details ------
Student ID : 101
Name       : YASH
Course     : BTECH
Marks      : 99
Result     : Pass

Enter Student ID : 47
Enter Name : VARDHAN
Enter Course : DATA SCIENCE
Enter Marks : 34

------ Student Details ------
Student ID : 47
Name       : VARDHAN
Course     : DATA SCIENCE
Marks      : 34
Result     : Fail
'''