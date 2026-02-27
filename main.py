# main.py

from cli import get_user_input
from normalizer import normalize_weights, normalize_scores
from scorer import compute_final_scores
from ranker import rank_courses
from explanation import generate_explanation

def main():
    criteria, courses = get_user_input()

    norm_weights = normalize_weights(criteria)
    norm_scores = normalize_scores(courses, criteria)
    final_scores = compute_final_scores(norm_scores, norm_weights)
    ranked = rank_courses(final_scores)

    print("\n=== Final Ranking ===")
    for i, (course, score) in enumerate(ranked, 1):
        print(f"{i}. {course} - Score: {score:.4f}")

    print("\n=== Explanation ===")
    explanation = generate_explanation(ranked, norm_scores, norm_weights)
    print(explanation)


if __name__ == "__main__":
    main()