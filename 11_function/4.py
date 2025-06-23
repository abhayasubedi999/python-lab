# Write lambda function to calculate square root of number

import math

num = int(input("Enter a number: "))
square_root = lambda num: math.sqrt(num)
print("Square root of", num, "is", square_root(num))
