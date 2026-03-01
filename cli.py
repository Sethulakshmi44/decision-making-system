# cli.py

from models import Criterion, Course

def safe_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def safe_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_user_input():
    criteria = []
    courses = []

    print("Welcome to Course Decision Companion")
    # --- Criteria Input ---
    n = safe_int_input("Enter number of criteria (Criteria is the features you want to consider): ")
    for _ in range(n):
        name = input("Criterion name: ")
        weight = safe_float_input("Weight (importance): ")
        crit_type = input("Type (benefit/cost): ").lower()
        criteria.append(Criterion(name, weight, crit_type))

    # --- Course Input ---
    m = safe_int_input("\nEnter number of courses: ")
    for _ in range(m):
        cname = input("\nCourse name: ")
        scores = {}
        for c in criteria:
            val = safe_float_input(f"Score for {c.name}: ")
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