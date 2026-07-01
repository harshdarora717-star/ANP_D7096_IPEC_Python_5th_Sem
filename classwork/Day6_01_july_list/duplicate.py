#wap to find the duplicate occurrences of a number in a list and remove them from the list

numbers = []

# Input 20 numbers
for i in range(20):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Original List:", numbers)

# Number to check
value = int(input("Enter number: "))

if value in numbers:
    first = numbers.index(value)   # First occurrence index

    for i in range(len(numbers) - 1, first, -1):
        if numbers[i] == value:
            numbers.pop(i)

    print("Duplicate occurrences removed.")
else:
    print("Number not found.")

print("Updated List:", numbers)