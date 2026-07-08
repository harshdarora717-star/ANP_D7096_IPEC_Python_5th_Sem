# Example 2: Using the numericcalc module from import statement
from numericcalc import calculate_sum, calculate_product, calculate_difference, calculate_division, calculate_modulus
a=5
b=10
print("sum of ",a," and ",b," is: ",calculate_sum(a,b))
print("product of ",a," and ",b," is: ",calculate_product(a,b))
print("difference of ",a," and ",b," is: ",calculate_difference(a,b))
print("division of ",a," and ",b," is: ",calculate_division(a,b))
print("modulus of ",a," and ",b," is: ",calculate_modulus(a,b))



#output:
'''
sum of  5  and  10  is:  15
product of  5  and  10  is:  50
difference of  5  and  10  is:  -5
division of  5  and  10  is:  0.5
modulus of  5  and  10  is:  5
'''