# Function to find the maximum number
def find_max(numbers):
    return max(numbers)


# Function to find the minimum number
def find_min(numbers):
    return min(numbers)


# Function to find the average
def find_average(numbers):
    return sum(numbers) / len(numbers)


# Main Program
numbers = []

# Accept 10 integers from the user
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Call the functions
maximum = find_max(numbers)
minimum = find_min(numbers)
average = find_average(numbers)

# Display the results
print("\nList:", numbers)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)
print("Average:", average)




#output:
'''
Enter number 1: 76
Enter number 2: 78
Enter number 3: 87
Enter number 4: 89
Enter number 5: 98
Enter number 6: 90
Enter number 7: 45
Enter number 8: 56
Enter number 9: 54
Enter number 10: 75

List: [76, 78, 87, 89, 98, 90, 45, 56, 54, 75]
Maximum Value: 98
Minimum Value: 45
Average: 74.8
'''