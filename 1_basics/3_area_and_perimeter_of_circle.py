# Calculate area & perimeter of circle based on diameter. (A=pi*r^2, P = 2*pi*r)
diameter = float(input("enter diameter of circle"))
radius = diameter / 2
PI = 3.1416
area = PI * radius**2
perimeter = 2 * PI * radius
print("perimeter :", perimeter)
print("area :", area)
