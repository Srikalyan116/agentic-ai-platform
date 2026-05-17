def calculate_priority_score(complexity: int, business_impact: int) -> int:
    """AI-style rule engine for priority scoring."""
    return min(100, (business_impact * 15) + (complexity * 8))


def build_recommendation(score: int) -> str:
    if score >= 80:
        return "Critical priority: assign senior engineer and review in daily stand-up."
    if score >= 55:
        return "Medium-high priority: plan implementation in the current sprint."
    if score >= 30:
        return "Normal priority: keep in backlog and monitor progress."
    return "Low priority: schedule after high-impact items are completed."
