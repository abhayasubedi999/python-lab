# Multiply numbers in a list using reduce function

from functools import reduce

numbers = [2, 3, 4, 5]

result = reduce(lambda x, y: x * y, numbers)
print(result)

result_with_init = reduce(lambda x, y: x * y, numbers, 1)
print(result_with_init)


def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst, 1)


print(multiply_list([1, 2, 3, 4]))
print(multiply_list([]))
