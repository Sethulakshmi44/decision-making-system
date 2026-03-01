# explanation.py

def generate_explanation(ranked, normalized_scores, normalized_weights, tolerance=1e-6):
    # Find all courses with rank 1
    top_courses = [course for rank, course, score, tie in ranked if rank == 1]

    if len(top_courses) > 1:
        explanation = "Top recommendation: " + " and ".join(top_courses)
        explanation += " (Tie)\n\n"
        explanation += "These courses achieved identical weighted scores.\n\n"
    else:
        explanation = f"Top recommendation: {top_courses[0]}\n\n"

    explanation += "Reasons:\n"

    for course in top_courses:
        explanation += f"\n--- {course} ---\n"
        contributions = []

        for crit, score in normalized_scores[course].items():
            weight = normalized_weights[crit]
            contribution = score * weight
            contributions.append((crit, contribution))

        contributions.sort(key=lambda x: x[1], reverse=True)

        for crit, contrib in contributions:
            explanation += f"- Strong impact from '{crit}' (impact: {contrib:.3f})\n"

    return explanation