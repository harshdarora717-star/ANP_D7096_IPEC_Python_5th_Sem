* **ANSWER 1:**



**# Electricity Bill Calculator**



units = int(input("Enter total electricity units: "))



\# Calculate bill

if units <= 100:

&#x20;   bill = units \* 5

elif units <= 200:

&#x20;   bill = (100 \* 5) + ((units - 100) \* 7)

else:

&#x20;   bill = (100 \* 5) + (100 \* 7) + ((units - 200) \* 10)



print("Bill Amount =", bill)



\# Apply 

if bill > 2000:

&#x20;   final\_bill = bill + (bill \* 5 / 100)

else:

&#x20;   final\_bill = bill



\# Minimum bill

if final\_bill < 500:

&#x20;   final\_bill = 500



print("Total Units =", units)

print("Final Payable Amount =", final\_bill)











* **ANSWER 2:**



**# Character Frequency Analyzer**



text = input("Enter a string: ")



uppercase = 0

lowercase = 0

digits = 0

special = 0



frequency = {}



for ch in text:

&#x20;   if ch.isupper():

&#x20;       uppercase += 1

&#x20;   elif ch.islower():

&#x20;       lowercase += 1

&#x20;   elif ch.isdigit():

&#x20;       digits += 1

&#x20;   else:

&#x20;       special += 1



&#x20;   if ch in frequency:

&#x20;       frequency\[ch] += 1

&#x20;   else:

&#x20;       frequency\[ch] = 1



\# Find most frequent character

most\_char = ""

max\_count = 0



for key in frequency:

&#x20;   if frequency\[key] > max\_count:

&#x20;       max\_count = frequency\[key]

&#x20;       most\_char = key



print("Uppercase :", uppercase)

print("Lowercase :", lowercase)

print("Digits :", digits)

print("Special Characters :", special)

print("Most Frequent Character :", most\_char)











* **ANSWER 3:**



**# Number Guessing Game**



secret\_number = 57

attempts = 0

max\_attempts = 7



while attempts < max\_attempts:

&#x20;   guess = int(input("Enter your guess: "))



&#x20;   if guess < 0:

&#x20;       print("Negative numbers are ignored.")

&#x20;       continue



&#x20;   attempts += 1



&#x20;   if guess == secret\_number:

&#x20;       print("Congratulations! You guessed the correct number.")

&#x20;       break

&#x20;   elif guess < secret\_number:

&#x20;       print("Too Low!")

&#x20;   else:

&#x20;       print("Too High!")



else:

&#x20;   print("Sorry! You have used all attempts.")



print("Attempts Used =", attempts)









* **ANSWER 4:**



**# Employee Salary Calculator**



def calculate\_da(basic):

&#x20;   return basic \* 0.10



def calculate\_tax(gross\_salary):

&#x20;   return gross\_salary \* 0.08



def calculate\_net\_salary(basic):

&#x20;   hra = basic \* 0.20

&#x20;   da = calculate\_da(basic)

&#x20;   gross\_salary = basic + hra + da

&#x20;   tax = calculate\_tax(gross\_salary)

&#x20;   net\_salary = gross\_salary - tax



&#x20;   print("\\nSalary Details")

&#x20;   print("Basic Salary :", basic)

&#x20;   print("HRA :", hra)

&#x20;   print("DA :", da)

&#x20;   print("Gross Salary :", gross\_salary)

&#x20;   print("Tax :", tax)

&#x20;   print("Net Salary :", net\_salary)



basic = float(input("Enter Basic Salary: "))

calculate\_net\_salary(basic)











* **ANSWER 5:**



**# List Processing**



numbers = \[]



print("Enter 20 integers:")



for i in range(20):

&#x20;   num = int(input())

&#x20;   numbers.append(num)



print("\\nOriginal List:", numbers)



\#  Largest Number

largest = max(numbers)

print("Largest Number:", largest)



\#  Second Largest Number

unique = list(set(numbers))

unique.sort()

print("Second Largest Number:", unique\[-2])



\#  Smallest Number

smallest = min(numbers)

print("Smallest Number:", smallest)



\#  Remove Duplicate Elements

print("List after removing duplicates:", unique)



\#  Print Even Numbers

print("Even Numbers:")

for num in numbers:

&#x20;   if num % 2 == 0:

&#x20;       print(num, end=" ")



\#  Numbers divisible by both 3 and 5

print("\\nNumbers divisible by both 3 and 5:")

for num in numbers:

&#x20;   if num % 3 == 0 and num % 5 == 0:

&#x20;       print(num, end=" ")



\#  Reverse without using reverse()

reversed\_list = \[]

for i in range(len(numbers)-1, -1, -1):

&#x20;   reversed\_list.append(numbers\[i])



print("\\nReversed List:", reversed\_list)











* **ANSWER 6:**



**# Tuple Operations**



students = (

&#x20;   "Aman", "Priya", "Rahul", "Neha", "Rohan",

&#x20;   "Ankit", "Pooja", "Riya", "Vikas", "Simran",

&#x20;   "Aman", "Karan", "Nisha", "Ritu", "Sahil"

)



\# Total students

print("Total Students:", len(students))



\# First five students

print("First Five Students:", students\[:5])



\# Last five students

print("Last Five Students:", students\[-5:])



\# Search a student

name = input("Enter student name to search: ")



if name in students:

&#x20;   print(name, "is present in the tuple.")

else:

&#x20;   print(name, "is not present in the tuple.")



\# Count occurrences

print("Occurrences of", name, "=", students.count(name))



\# Convert tuple to list and sort

student\_list = list(students)

student\_list.sort()



print("Students in Alphabetical Order:")

print(student\_list)









* **ANSWER 7:**



**# Student Result Management**



students = {}



print("Enter marks of 10 students:")



for i in range(10):

&#x20;   roll = input("Enter Roll Number: ")

&#x20;   marks = int(input("Enter Marks: "))

&#x20;   students\[roll] = marks



\# Find topper

topper = max(students, key=students.get)

print("\\nTopper Roll No:", topper)

print("Top Marks:", students\[topper])



\# Average Marks

average = sum(students.values()) / len(students)

print("Average Marks:", average)



\# Students scoring above average

print("Students scoring above average:")

for roll, marks in students.items():

&#x20;   if marks > average:

&#x20;       print(roll, ":", marks)



\# Count failed students

failed = 0

for marks in students.values():

&#x20;   if marks < 35:

&#x20;       failed += 1



print("Failed Students:", failed)



\# Display Grades

print("\\nStudent Grades")



for roll, marks in students.items():



&#x20;   if marks >= 90:

&#x20;       grade = "A+"

&#x20;   elif marks >= 75:

&#x20;       grade = "A"

&#x20;   elif marks >= 60:

&#x20;       grade = "B"

&#x20;   elif marks >= 45:

&#x20;       grade = "C"

&#x20;   elif marks >= 35:

&#x20;       grade = "D"

&#x20;   else:

&#x20;       grade = "F"



&#x20;   print("Roll No:", roll, "Marks:", marks, "Grade:", grade)













* **ANSWER 8:**



**# Password Strength Checker**



password = input("Enter Password: ")



missing = \[]



\# Minimum length

if len(password) < 8:

&#x20;   missing.append("Minimum 8 characters")



\# Uppercase letter

upper = False

for ch in password:

&#x20;   if ch.isupper():

&#x20;       upper = True

&#x20;       break

if not upper:

&#x20;   missing.append("At least one uppercase letter")



\# Lowercase letter

lower = False

for ch in password:

&#x20;   if ch.islower():

&#x20;       lower = True

&#x20;       break

if not lower:

&#x20;   missing.append("At least one lowercase letter")



\# Digit

digit = False

for ch in password:

&#x20;   if ch.isdigit():

&#x20;       digit = True

&#x20;       break

if not digit:

&#x20;   missing.append("At least one digit")



\# Special character

special = False

for ch in password:

&#x20;   if not ch.isalnum():

&#x20;       special = True

&#x20;       break

if not special:

&#x20;   missing.append("At least one special character")



\# Result

if len(missing) == 0:

&#x20;   print("Strong Password")

else:

&#x20;   print("Weak Password")

&#x20;   print("Missing Conditions:")

&#x20;   for item in missing:

&#x20;       print("-", item)











* **ANSWER 9:**



**# Word Frequency Counter**



def word\_frequency(sentence):



&#x20;   # Remove punctuation

&#x20;   punctuation = ".,!?;:'\\"()-"



&#x20;   for ch in punctuation:

&#x20;       sentence = sentence.replace(ch, "")



&#x20;   # Convert to lowercase

&#x20;   sentence = sentence.lower()



&#x20;   # Convert into list of words

&#x20;   words = sentence.split()



&#x20;   # Dictionary for frequency

&#x20;   frequency = {}



&#x20;   for word in words:

&#x20;       if word in frequency:

&#x20;           frequency\[word] += 1

&#x20;       else:

&#x20;           frequency\[word] = 1



&#x20;   # Display in alphabetical order

&#x20;   print("\\nWord Frequency:")



&#x20;   for word in sorted(frequency):

&#x20;       print(word, ":", frequency\[word])



&#x20;   # Find most repeated word

&#x20;   most\_word = max(frequency, key=frequency.get)



&#x20;   print("\\nMost Repeated Word:", most\_word)





\# Main Program

sentence = input("Enter a sentence: ")

word\_frequency(sentence)











* **ANSWER 10:**



**# Student Record Management System**



students = \[]



\# 1. Add Student

def add\_student():

&#x20;   roll = input("Enter Roll Number: ")



&#x20;   # Check duplicate roll number

&#x20;   for student in students:

&#x20;       if student\["Roll"] == roll:

&#x20;           print("Roll Number already exists!")

&#x20;           return



&#x20;   name = input("Enter Name: ")

&#x20;   age = int(input("Enter Age: "))

&#x20;   course = input("Enter Course: ")

&#x20;   marks = float(input("Enter Marks: "))



&#x20;   student = {

&#x20;       "Roll": roll,

&#x20;       "Name": name,

&#x20;       "Age": age,

&#x20;       "Course": course,

&#x20;       "Marks": marks

&#x20;   }



&#x20;   students.append(student)

&#x20;   print("Student Added Successfully!")



\# 2. Display All Students

def display\_students():

&#x20;   if len(students) == 0:

&#x20;       print("No Records Found!")

&#x20;       return



&#x20;   print("\\nStudent Records")

&#x20;   for student in students:

&#x20;       print(student)



\# 3. Search Student

def search\_student():

&#x20;   roll = input("Enter Roll Number: ")



&#x20;   for student in students:

&#x20;       if student\["Roll"] == roll:

&#x20;           print(student)

&#x20;           return



&#x20;   print("Student Not Found!")



\# 4. Update Marks

def update\_marks():

&#x20;   roll = input("Enter Roll Number: ")



&#x20;   for student in students:

&#x20;       if student\["Roll"] == roll:

&#x20;           marks = float(input("Enter New Marks: "))

&#x20;           student\["Marks"] = marks

&#x20;           print("Marks Updated Successfully!")

&#x20;           return



&#x20;   print("Student Not Found!")



\# 5. Delete Student

def delete\_student():

&#x20;   roll = input("Enter Roll Number: ")



&#x20;   for student in students:

&#x20;       if student\["Roll"] == roll:

&#x20;           students.remove(student)

&#x20;           print("Student Deleted Successfully!")

&#x20;           return



&#x20;   print("Student Not Found!")



\# 6. Display Topper

def display\_topper():

&#x20;   if len(students) == 0:

&#x20;       print("No Records Found!")

&#x20;       return



&#x20;   topper = max(students, key=lambda x: x\["Marks"])



&#x20;   print("\\nTopper Details")

&#x20;   print(topper)



\# 7. Display Average Marks

def average\_marks():

&#x20;   if len(students) == 0:

&#x20;       print("No Records Found!")

&#x20;       return



&#x20;   total = 0



&#x20;   for student in students:

&#x20;       total += student\["Marks"]



&#x20;   average = total / len(students)



&#x20;   print("Average Marks =", average)



\# 8. Students Above Average

def above\_average():

&#x20;   if len(students) == 0:

&#x20;       print("No Records Found!")

&#x20;       return



&#x20;   total = 0



&#x20;   for student in students:

&#x20;       total += student\["Marks"]



&#x20;   average = total / len(students)



&#x20;   print("Students Above Average")



&#x20;   for student in students:

&#x20;       if student\["Marks"] > average:

&#x20;           print(student)



\# Main Menu

while True:



&#x20;   print("\\n===== Student Record Management System =====")

&#x20;   print("1. Add Student")

&#x20;   print("2. Display All Students")

&#x20;   print("3. Search Student by Roll Number")

&#x20;   print("4. Update Marks")

&#x20;   print("5. Delete Student")

&#x20;   print("6. Display Topper")

&#x20;   print("7. Display Average Marks")

&#x20;   print("8. Display Students Above Average")

&#x20;   print("9. Exit")



&#x20;   choice = int(input("Enter your choice: "))



&#x20;   if choice == 1:

&#x20;       add\_student()



&#x20;   elif choice == 2:

&#x20;       display\_students()



&#x20;   elif choice == 3:

&#x20;       search\_student()



&#x20;   elif choice == 4:

&#x20;       update\_marks()



&#x20;   elif choice == 5:

&#x20;       delete\_student()



&#x20;   elif choice == 6:

&#x20;       display\_topper()



&#x20;   elif choice == 7:

&#x20;       average\_marks()



&#x20;   elif choice == 8:

&#x20;       above\_average()



&#x20;   elif choice == 9:

&#x20;       print("Thank You!")

&#x20;       break



&#x20;   else:

&#x20;       print("Invalid Choice! Please Try Again.")





