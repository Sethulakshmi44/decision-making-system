# scorer.py

def compute_final_scores(normalized_scores, normalized_weights):
    final_scores = {}

    for course, scores in normalized_scores.items():
        total = 0
        for crit, score in scores.items():
            total += score * normalized_weights[crit]
        final_scores[course] = total

    return final_scores