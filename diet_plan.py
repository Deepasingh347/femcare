def get_personalized_plan(symptom_type):
    plans = {
        "insulin": {
            "diet": "Low-carb, high-protein meals. Avoid sugar & refined carbs. Include cinnamon, flax seeds, lean protein.",
            "workout": "30 mins cardio + strength training (4 days/week)"
        },
        "inflammation": {
            "diet": "Anti-inflammatory foods: turmeric, leafy greens, berries, omega-3-rich meals.",
            "workout": "Gentle yoga or pilates + walk 5 days/week"
        },
        "hormonal": {
            "diet": "Balanced macros: complex carbs, protein, healthy fats. Avoid dairy and caffeine.",
            "workout": "Cycle syncing workouts (HIIT in follicular, yoga in luteal phase)"
        }
    }
    return plans.get(symptom_type, {})
