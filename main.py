# main.py

from cli import get_user_input
from normalizer import normalize_weights, normalize_scores
from scorer import compute_final_scores
from ranker import rank_courses
from explanation import generate_explanation
from constraints import apply_constraints


def main():
    criteria, courses, constraints = get_user_input()

    if len(criteria) == 0:
        print("\nError: At least one criterion is required to evaluate courses.")
        return

    if len(courses) == 0:
        print("\nError: At least one course must be entered.")
        return
    # Apply constraints BEFORE scoring
    if constraints:
        filtered_courses = apply_constraints(courses, constraints)
        removed = len(courses) - len(filtered_courses)

        print(f"\nFiltered out {removed} course(s) based on constraints.")

        if not filtered_courses:
            print("No courses satisfy the constraints.")
            return

        courses = filtered_courses

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