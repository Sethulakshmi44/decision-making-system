# cli.py

from models import Criterion, Course


def get_user_input():
    criteria = []
    courses = []

    # --- Criteria Input ---
    n = int(input("Enter number of criteria: "))
    for _ in range(n):
        name = input("Criterion name: ")
        weight = float(input("Weight (importance): "))
        crit_type = input("Type (benefit/cost): ").lower()
        criteria.append(Criterion(name, weight, crit_type))

    # --- Course Input ---
    m = int(input("\nEnter number of courses: "))
    for _ in range(m):
        cname = input("\nCourse name: ")
        scores = {}
        for c in criteria:
            val = float(input(f"Score for {c.name}: "))
            scores[c.name] = val
        courses.append(Course(cname, scores))

    # --- Constraints Input ---
    constraints = {}

    use_constraints = input("\nDo you want to add hard constraints? (yes/no): ").lower()

    if use_constraints == "yes":
        num_constraints = int(input("How many constraints?: "))

        for _ in range(num_constraints):
            crit_name = input("Constraint criterion name: ")
            condition = input("Condition (<=, >=): ")
            value = float(input("Value: "))

            if condition == "<=":
                constraints[crit_name] = lambda x, v=value: x <= v
            elif condition == ">=":
                constraints[crit_name] = lambda x, v=value: x >= v

    return criteria, courses, constraints