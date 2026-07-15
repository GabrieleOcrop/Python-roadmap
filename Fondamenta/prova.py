def score_life_style_calculator(daily_steps_score, workouts_per_week_score):
    return ((daily_steps_score + workouts_per_week_score) / 2)

daily_steps_score = 5
workouts_per_week_score = 2

value = score_life_style_calculator(daily_steps_score, workouts_per_week_score)

print(value)
