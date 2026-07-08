#module to contain numeric calculations
def calculate_sum(a, b):
    return (a + b)

def calculate_product(a, b):
    return (a * b)

def calculate_difference(a, b):
    return (a - b)

def calculate_division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return (a / b)

def calculate_modulus(a, b):
    if b == 0:
        return "Error: Division by zero"
    return (a % b)



#output:
'''
sum of  5  and  10  is:  15
product of  5  and  10  is:  50
difference of  5  and  10  is:  -5
division of  5  and  10  is:  0.5
modulus of  5  and  10  is:  5
'''
