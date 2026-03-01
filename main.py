from cli import get_user_input
from normalizer import normalize_weights, normalize_scores
from scorer import compute_final_scores
from ranker import rank_courses
from explanation import generate_explanation
from constraints import apply_constraints


def main():

    criteria, courses, constraints = get_user_input()

    if len(criteria) == 0:
        print("Error: At least one criterion required.")
        return

    if constraints:
        courses = apply_constraints(courses, constraints)
        if not courses:
            print("No courses satisfy constraints.")
            return

    norm_weights = normalize_weights(criteria)
    norm_scores = normalize_scores(courses, criteria)
    final_scores = compute_final_scores(norm_scores, norm_weights)
    ranked = rank_courses(final_scores)

    print("\n=== Final Ranking ===")
    for rank, course, score, tie in ranked:
        tie_text = " (Tied)" if tie else ""
        print(f"{rank}. {course} - Score: {score:.4f}{tie_text}")

    print("\n=== Explanation ===")
    explanation = generate_explanation(ranked, norm_scores, norm_weights)
    print(explanation)


if __name__ == "__main__":
    main()