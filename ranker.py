# ranker.py

def rank_courses(final_scores):
    return sorted(final_scores.items(), key=lambda x: x[1], reverse=True)