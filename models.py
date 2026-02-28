# models.py

class Criterion:
    def __init__(self, name, weight, crit_type):
        """
        crit_type: 'benefit' or 'cost'
        """
        self.name = name
        self.weight = weight
        self.crit_type = crit_type


class Course:
    def __init__(self, name, scores):
        """
        scores: dict of {criterion_name: value}
        """
        self.name = name
        self.scores = scores