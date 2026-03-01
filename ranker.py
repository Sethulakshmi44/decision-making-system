# ranker.py

def rank_courses(final_scores, tolerance=1e-6):
    sorted_courses = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)

    ranked = []
    current_rank = 1

    for i, (course, score) in enumerate(sorted_courses):
        if i > 0 and abs(score - sorted_courses[i-1][1]) < tolerance:
            # Tie detected
            ranked.append((current_rank, course, score, "TIE"))
        else:
            current_rank = i + 1
            ranked.append((current_rank, course, score, ""))

    return ranked