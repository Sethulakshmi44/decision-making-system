# explanation.py

def generate_explanation(ranked, normalized_scores, normalized_weights):
    top_course = ranked[0][0]
    reasons = []

    for crit, score in normalized_scores[top_course].items():
        weight = normalized_weights[crit]
        contribution = score * weight
        reasons.append((crit, contribution))

    reasons.sort(key=lambda x: x[1], reverse=True)

    explanation = f"Top recommendation: {top_course}\n\nReasons:\n"
    for crit, contrib in reasons:
        explanation += f"- Strong performance in '{crit}' (impact: {contrib:.2f})\n"

    return explanation