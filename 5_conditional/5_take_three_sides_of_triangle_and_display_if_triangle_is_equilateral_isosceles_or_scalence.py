first_side = int(input("enter first side of triangle : "))
second_side = int(input("enter second side of triangle : "))
third_side = int(input("enter third side of triangle : "))
if first_side == second_side == third_side:
    print("the given triangle is equilateral triangle")
elif first_side == second_side or second_side == third_side or first_side == third_side:
    print("the given triangle is isosceles triangle")
else:
    print("the given triangle is scalene triangle")
