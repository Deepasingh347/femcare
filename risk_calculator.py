def calculate_pcos_risk(responses):
    score = 0
    for key, answer in responses.items():
        if answer.lower() == "yes":
            score += 1

    if score >= 4:
        return "High"
    elif score == 2 or score == 3:
        return "Moderate"
    else:
        return "Low"
