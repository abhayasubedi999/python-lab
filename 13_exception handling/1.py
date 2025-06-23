# Write a function can_drink that takes age as argument checks if user can drink. If user is 18+, return True else return False. Note: You need to raise TypeError if age is not integer value, ValueError if age is below 0, AssertionError if age is above 100.


def can_drink(age):
    # Check if age is an integer
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    # Check if age is negative
    if age < 0:
        raise ValueError("Age cannot be negative")

    # Check if age is above 100
    assert age <= 100, "Age cannot be above 100"

    # Check if age is 18 or above
    return age >= 18


try:
    age = int(input("Enter your age: "))
    if can_drink(age):
        print("You can drink")
    else:
        print("You cannot drink")
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except AssertionError as e:
    print(e)
