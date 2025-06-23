# Store the marks of student in a list called student_marks. You need to store marks of 5 subjects. If marks in either of the subject is below 40 display, You’ve failed but if marks in all subject is above 40 display the grade as Congratulations !! You’ve passed in grade {calculated_grade}
maths = int(input("enter your marks in maths: "))
english = int(input("enter your marks in english: "))
nepali = int(input("enter your marks in nepali: "))
computer = int(input("enter your marks in computer: "))
science = int(input("enter your marks in science: "))
student_marks = [maths, english, nepali, computer, science]
has_failed = any(mark < 40 for mark in student_marks)
if has_failed:
    print("You've failed")
else:
    average_marks = sum(student_marks) / len(student_marks)
    if average_marks >= 90:
        grade = "A+"
    elif average_marks >= 80:
        grade = "A"
    elif average_marks >= 70:
        grade = "B"
    elif average_marks >= 60:
        grade = "C"
    elif average_marks >= 50:
        grade = "D"
    else:
        grade = "E"
    print(f"Congratulations !! You've passed in grade {grade}")
