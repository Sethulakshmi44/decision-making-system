# cli.py

from models import Criterion, Course

def get_user_input():
    criteria = []
    courses = []

    n = int(input("Enter number of criteria: "))
    for _ in range(n):
        name = input("Criterion name: ")
        weight = float(input("Weight (importance): "))
        crit_type = input("Type (benefit/cost): ")
        criteria.append(Criterion(name, weight, crit_type))

    m = int(input("\nEnter number of courses: "))
    for _ in range(m):
        cname = input("\nCourse name: ")
        scores = {}
        for c in criteria:
            val = float(input(f"Score for {c.name}: "))
            scores[c.name] = val
        courses.append(Course(cname, scores))

    return criteria, courses