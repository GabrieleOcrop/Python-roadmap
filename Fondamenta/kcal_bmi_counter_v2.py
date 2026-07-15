import os

#sets for user responses
allowed_yes_responses = {"yes", "yep", "y", "sure"}
allowed_no_responses = {"no", "nop", "n", "negative"}
allowed_genre_responses = {"male", "female", "m", "f"}

#functions

#for cleaning console 
def clear_console():
    # 'cls' is for Windows, 'clear' is for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def get_name():
    while True:
        name = input("What's your name? :").strip()
        if not name:
            print("Name field cannot be empty!")
        elif (len(name) < 3) or (len(name) > 16):
            print("Name field lenght must be from 3 to 16 characters")
        elif any(char.isdigit() for char in name):
            print("Name field cannot accept numbers")
        else:
            return name

def get_genre():
    while True:
        genre = input("Are you male or female? :")
        if not genre:
            print("Genre field cannot be empty!")
        elif genre.strip().lower() not in allowed_genre_responses:
            print("genre field accept only male/female genres! Don't get offended :|")
        else:
            return genre

def get_age():
    while True:
        age = input("How old are you? :")
        if not age:
            print("Age field cannot be empty!")
        elif not age.isdigit(): #is the string age full of numbers? yes; there are some characters into the string? error
            print("Stop playing dude -.-")
        elif (int(age) < 4):
            print("You are too child to use that! Go play around!")
        elif (int(age) > 110):
            print("Seems to be an error in age input!")
        else:
            return int(age)


def get_height():
    while True:
        height = input("How tall are you? Be sure that's in centimeters! :")
        if not height:
            print("Height field cannot be empty!")
        elif not height.isdigit():
            print("Stop playing dude -.-")
        else:
            asking = input("Are you sure that you put the right value? :")
            if asking.lower() in allowed_yes_responses:
                return int(height)

def get_weight():
    while True:
        weight = input("How much do you weight? Be sure that's in kilograms! :")
        if not weight:
            print("Weight field cannot be empty!")
        elif not weight.replace(".", "", 1).isdigit():
            print("Stop playing dude -.-")
        else:
            asking = input("Are you sure that you put the right value? :")
            if asking.lower() in allowed_yes_responses:
                return float(weight)

def get_workouts_per_week():
    while True:
        workouts_per_week = input("How many workouts do you do per week? :")
        if not workouts_per_week:
            print("Number of workouts per week field cannot be empty!")
        elif not workouts_per_week.isdigit():
            print("stop playing dude -.-")
        elif (int(workouts_per_week) < 0):
            print("Please stop! You can't do negative workouts!")
        elif (int(workouts_per_week) > 7):
            print("I dunno if you are too crazy to do this shit! Please take a team and don't use this crap! or revise :)")
        else:
            return int(workouts_per_week)

        


def get_numero_daily_steps():
    while True:
        daily_steps = input("How many steps do you usually take each day? :")
        if not daily_steps:
            print("passi giornalieri field cannot be empty!")
        elif not daily_steps.isdigit():
            print("stop playing dude! -.-")
        elif (int(daily_steps) > 20000):
            print("I dunno if you are too crazy to do this shit! Please take a team and don't use this crap! or revise :)")
        else:
            return int(daily_steps)


def male_kcal(age,height,weight):
    return (
            (10*weight) 
            + (6.25*height) 
            - (5*age) 
            + 5
            )

def female_kcal(age,height,weight):
    return (
            (10*weight)
            + (6.25*height) 
            - (5*age) 
            - 161
            )

def bmi_calculation(height,weight):
    return (
        weight / ((height / 100) ** 2)
    )

def daily_steps_score_calculator(daily_steps):
    if daily_steps >= 10000:
        return 5
    elif daily_steps >= 7500:
        return 4
    elif daily_steps >= 5000:
        return 3
    elif daily_steps >= 2500:
        return 2
    elif daily_steps < 2500:
        return 1
    
def workouts_per_week_calculator(workouts_per_week):
    if workouts_per_week >= 5:
        return 5
    elif workouts_per_week == 4:
        return 4
    elif workouts_per_week == 3:
        return 3
    elif workouts_per_week == 2:
        return 2
    elif workouts_per_week == 1:
        return 1
    elif workouts_per_week == 0:
        return 0
    
def score_life_style_calculator(daily_steps_score, workouts_per_week_score):
    return ((daily_steps_score + workouts_per_week_score) / 2)

def TDEE_calculator(life_style_score, kcal_value):
    if life_style_score >= 5: 
        return  kcal_value * 1.9
    elif 4 <= life_style_score and life_style_score < 5:
        return  kcal_value * 1.725
    elif 3 <= life_style_score and life_style_score < 4:
        return  kcal_value * 1.55
    elif 2 <= life_style_score and life_style_score < 3:
        return  kcal_value * 1.375
    elif 0 <= life_style_score and life_style_score < 2:
        return  kcal_value * 1.2
    
    

#main program
clear_console()

print("Kcal, bmi and TDEE counter v3 made by nothing to do!")
while True:
    name = get_name()
    genre = get_genre()
    age = get_age()
    height = get_height()
    weight = get_weight()
    daily_steps = get_numero_daily_steps()
    workouts_per_week = get_workouts_per_week()

    daily_steps_score = daily_steps_score_calculator(daily_steps)
    workouts_per_week_score = workouts_per_week_calculator(workouts_per_week)
    life_style_score = score_life_style_calculator(daily_steps_score, workouts_per_week_score)
    
    input_data = f'Your name is {name} and you are a {genre}. You are {age} years old, you are tall {height}cm and your weight is {weight}kgs. \n Your daily steps is around {daily_steps} and you do {workouts_per_week} workouts every week'
    print(input_data) 
    choose = input("That's correct? :").lower()
    if choose.lower() in allowed_yes_responses:
        bmi_value = bmi_calculation(height,weight)
        if genre.strip().lower() == "female" or genre.strip().lower() == "f":
            kcal_value = female_kcal(age, height, weight)
            TDEE = TDEE_calculator(life_style_score, kcal_value)
            message = f'Your BMI is {bmi_value:.2f} and your BMR {round(kcal_value)} per day! \n Your life_style score is {life_style_score} so you have to stay around {round(TDEE)} kcals per day!'
            print(message)
            break
        elif genre.strip().lower() == "male" or genre.strip().lower() == "m":
            kcal_value = male_kcal(age, height, weight)
            TDEE = TDEE_calculator(life_style_score, kcal_value)
            message = f'Your BMI is {bmi_value:.2f} and your BMR {round(kcal_value)} per day! \n Your movement score is {life_style_score} so you have to stay around {round(TDEE)} kcals per day!'
            print(message)
            break
    elif choose.lower() in allowed_no_responses:
        continue
    else:
        break

