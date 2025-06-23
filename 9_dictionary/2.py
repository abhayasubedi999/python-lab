# ​Broadway_1 has course as {‘python’: {‘duration’: 3, ‘type’: ‘basic’}, ‘java’: {‘duration’: 4, ‘type’: ‘medium’}}. Broadway_2 has course as {‘multimedia’: {‘duration’: 2, ‘type’: ‘basic’}}. Broadway_1 and Broadway_2 has been merged. Combine the course offered by this new institute and display them

broadway_1 = {
    "python": {"duration": 3, "type": "basic"},
    "java": {"duration": 4, "type": "medium"},
}
broadway_2 = {"multimedia": {"duration": 2, "type": "basic"}}

merged_courses = {**broadway_1, **broadway_2}

print("Combined Courses:")
for course, details in merged_courses.items():
    print(f"Course: {course}")
    print(f"Duration: {details['duration']} months")
    print(f"Type: {details['type']}\n")
