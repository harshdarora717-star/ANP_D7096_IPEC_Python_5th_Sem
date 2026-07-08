#in this the operations are performed on the 2d figures 
# like rectangle, square, circle and triangle
from prompt_toolkit import choice

from twodfigures import *

print("===== Geometry Calculator =====")
print("1. Square")
print("2. Circle")
print("3. Triangle")
print("4. Rectangle")



# do{ # type: ignore

choice = int(input("Enter your choice: "))

if choice == 1: # type: ignore
    side = float(input("Enter side of the square: "))
    ch = int (input("Enter 1 for area and 2 for perimeter: "))
    if ch == 1:
        print("Area =", square_area(side))
    elif ch == 2:
        print("Perimeter =", square_perimeter(side))

elif choice == 2:
    radius = float(input("Enter radius of the circle: "))
    ch = int(input("Enter 1 for area and 2 for circumference: "))
    if ch == 1:
        print("Area =", circle_area(radius))
    elif ch == 2:
        print("Circumference =", circle_perimeter(radius))

elif choice == 3:
    base = float(input("Enter base of the triangle: "))
    height = float(input("Enter height of the triangle: "))
    side1 = float(input("Enter side1 of the triangle: "))
    side2 = float(input("Enter side2 of the triangle: "))
    side3 = float(input("Enter side3 of the triangle: "))

    ch = int(input("Enter 1 for area and 2 for perimeter: "))
    if ch == 1:
        print("Area =", triangle_area(base, height))
    elif ch == 2:
        print("Perimeter =", triangle_perimeter(side1, side2, side3))

elif choice == 4:
    length = float(input("Enter length of the rectangle: "))
    breadth = float(input("Enter breadth of the rectangle: "))

    ch = int(input("Enter 1 for area and 2 for perimeter: "))
    if ch == 1:
        print("Area =", rectangle_area(length, breadth))
    elif ch == 2:
        print("Perimeter =", rectangle_perimeter(length, breadth))

else:
    print("Invalid Choice")
# }while (choice != 0)