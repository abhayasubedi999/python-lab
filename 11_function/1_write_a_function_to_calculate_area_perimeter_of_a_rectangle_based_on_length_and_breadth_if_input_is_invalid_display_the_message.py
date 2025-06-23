# Write a function to calculate area & perimeter of a rectangle based on length and breadth. If input is invalid display the message (int is valid)


def area_perimeter(length, breadth):
    if type(length) == int and type(breadth) == int:
        area = length * breadth
        perimeter = 2 * (length + breadth)
        print(f"area of rectangle is {area}")
        print(f"perimeter of rectangle is {perimeter}")
    else:
        print("invalid input")


length = int(input("enter the length: "))
breadth = int(input("enter the breadth: "))
area_perimeter(length, breadth)
