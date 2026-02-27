# normalizer.py

def normalize_weights(criteria):
    total = sum(c.weight for c in criteria)
    return {c.name: c.weight / total for c in criteria}


def normalize_scores(courses, criteria):
    normalized = {course.name: {} for course in courses}

    for crit in criteria:
        values = [course.scores[crit.name] for course in courses]

        if crit.crit_type == "benefit":
            max_val = max(values)
            for course in courses:
                normalized[course.name][crit.name] = course.scores[crit.name] / max_val
        else:  # cost
            min_val = min(values)
            for course in courses:
                normalized[course.name][crit.name] = min_val / course.scores[crit.name]

    return normalized