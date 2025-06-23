# area_and_perimeter_of_circle_based_in_diameter
diameter = float(input("enter the diameter: "))
radius = diameter / 2
PI = 3.1416
area = PI * radius**2
perimeter = 2 * PI * radius
print("""the area is :{area}""".format(area=area))
print("""the perimeter is :{perimeter}""".format(perimeter=perimeter))
