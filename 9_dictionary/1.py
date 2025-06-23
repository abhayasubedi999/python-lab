# Broadway offer courses, store them as format: {‘course’: [‘Python’, ‘Java’], ‘duration’: [3, 4]}. Check and display if ‘Python’ is offered course.

courses = {"course": ["Python", "Java"], "duration": [3, 4]}

if "Python" in courses["course"]:
    print("'Python' is an offered course.")
else:
    print("'Python' is not an offered course.")
