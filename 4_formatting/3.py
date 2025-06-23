# Take input of name & marks. Display percentage obtained. Output Format: Ram, you have scored 85.23% in exam.​

name = input("Enter your name: ")
obtained_marks = float(input("Enter your marks: "))
full_marks = 100
percentage = (obtained_marks / full_marks) * 100
print(f"{name}, you have scored {percentage}% in exam.")
