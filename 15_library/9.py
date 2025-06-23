# Calculate LCM of numbers present in a list
import numpy as numpy


def lcm_of_list(numbers):
    return numpy.lcm.reduce(numbers)


numbers = [12, 15, 20, 30]
print(f"LCM: {lcm_of_list(numbers)}")
