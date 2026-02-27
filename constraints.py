# constraints.py

def apply_constraints(courses, constraints):
    """
    constraints example:
    {
        "Cost": lambda x: x <= 5000
    }
    """
    filtered = []

    for course in courses:
        valid = True
        for crit, rule in constraints.items():
            if crit in course.scores:
                if not rule(course.scores[crit]):
                    valid = False
        if valid:
            filtered.append(course)

    return filtered