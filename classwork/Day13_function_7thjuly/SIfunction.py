# Simple Interest Calculator using Function

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("Enter the principal (in rs): "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))
print("Simple Interest:", calculate_simple_interest(principal, rate, time))

#output:
'''
Enter the principal (in rs): 10000
Enter the rate of interest (in %): 5
Enter the time (in years): 2
Simple Interest: 1000.0
'''