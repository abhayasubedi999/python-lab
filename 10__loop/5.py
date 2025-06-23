# Your list contains marks scored by students. Display the second highest number from it

marks = [90, 20, 30, 40, 50, 60, 70, 80, 10, 100, 100, 100]
marks = list(set(marks))
marks.sort()
print(marks[-2])
