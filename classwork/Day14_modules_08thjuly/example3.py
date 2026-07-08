# Example 3: using some specific functions from the numericcalc module
from numericcalc import calculate_sum

a = 5
b = 10
print("sum of ", a, " and ", b, " is: ", calculate_sum(a, b))

#m=50
#n=40
#print("difference of ", m, " and ", n, " is: ", calculate_difference(m, n))  
# This will raise an error since calculate_difference is not imported


#output:
'''
sum of  5  and  10  is:  15
Traceback (most recent call last):
  File "d:\ANP_D7096_IPEC_Python_5th_Sem\classwork\Day14_modules_08thjuly\example3.py", line 10, in <module>
    print("difference of ", m, " and ", n, " is: ", calculate_difference(m, n))
    '''