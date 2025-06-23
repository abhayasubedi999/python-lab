# Write a function that take name of student and course enrolled as input and display: Hello {std}, Welcome to course {course}. If course is not passed to function it has to be python in default


def welcome(std, course="python"):
    return f" Hello {std}, Welcome to course {course}"


std = input("enter your name: ")
print(welcome(std))
