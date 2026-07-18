
# WAP to display the first name without using library functions

name = input("Enter your full name: ")

first_name = ""

for x in name:
    if x == ' ':
        break
    first_name = first_name + x

print("First Name =", first_name)