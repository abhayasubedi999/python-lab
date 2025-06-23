# Record of student is stored as {‘9843’: {‘course’: ‘python’, ‘name’: ‘abc’, ‘present’: True}, ‘984’: {‘course’: ‘c’, ‘name’: ‘efg’, ‘present’: False}}. Display name of student who are absent in python class

student_records = {
    "9843": {"course": "python", "name": "abc", "present": True},
    "984": {"course": "c", "name": "efg", "present": False},
    "985": {
        "course": "python",
        "name": "abhaya",
        "present": True,
    },
}

absent_python_students = []

for student_id, details in student_records.items():
    if details["course"].lower() == "python" and not details["present"]:
        absent_python_students.append(details["name"])

if absent_python_students:
    print("Absent students in Python class:", ", ".join(absent_python_students))
else:
    print("No students are absent in Python class.")
