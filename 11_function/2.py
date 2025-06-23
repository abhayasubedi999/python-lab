# Write a function sum_all that takes any number of numeric argument and display the sum


def sum_all(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


args = [1, 2, 3, 75]
print(sum_all(*args))
