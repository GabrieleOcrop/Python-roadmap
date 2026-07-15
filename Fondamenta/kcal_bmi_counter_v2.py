import os

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
        genre = input("Are you male or female? :").strip()
        if not genre:
            print("Genre field cannot be empty!")
        elif ("male" not in genre.replace(" ", "").lower() and "female" not in genre.replace(" ", "").lower() ):
            print("genre field doesn't accept other genres!")
        elif any(char.isdigit() for char in name):
            print("Genre field doesn't accept numbers")
        elif (genre == "m" or genre == "M" or genre == "f" or genre == "F"):
            return genre
        else:
            return genre

def get_age():
    while True:
        age = int(input("How old are you? :"))
        if not age:
            print("Age field cannot be empty!")
        elif (age < 4):
            print("You are too child to use that! Go play around!")
        elif (age > 110):
            print("Seems to be an error in age input!")
        else:
            return age


def get_height():
    while True:
        height = float(input("How tall are you? Be sure that's in centimeters! :"))
        if not height:
            print("Height field cannot be empty!")
        else:
            asking = input("Are you sure that you put the right value? :").lower().strip().replace(" ", "")
            if "yes" in asking or "yeah" in asking or "yeh" in asking:
                return height
            else:
                False

def get_weight():
    while True:
        weight = float(input("How much do you weight? Be sure that's in kilograms! :"))
        if not weight:
            print("Weight field cannot be empty!")
        else:
            asking = input("Are you sure that you put the right value? :").lower().strip().replace(" ", "")
            if "yes" in asking or "yeah" in asking or "yeh" in asking:
                return weight
            else:
                False

def get_workouts_per_week():
    while True:
        workouts_per_week = int(input("How many workouts do you do per week? :"))
        if not workouts_per_week:
            print("Number of workouts per week field cannot be empty!")
        elif (workouts_per_week < 0):
            print("Please stop! You can't do negative workouts!")
        elif (workouts_per_week > 7):
            print("I dunno if you are too crazy to do this shit! Please take a team and don't use this crap! or revise :)")
        else:
            return workouts_per_week

        


def get_numero_daily_steps():
    while True:
        daily_steps = int(input("How many steps do you usually take each day? :"))
        if not daily_steps:
            print("passi giornalieri field cannot be empty!")
        elif (daily_steps < 0):
            print("Please stop! You can't take negative steps!")
        elif (daily_steps > 20000):
            print("I dunno if you are too crazy to do this shit! Please take a team and don't use this crap! or revise :)")
        else:
            return daily_steps


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
    elif daily_steps > 7500 and daily_steps < 10000:
        return 4
    elif daily_steps > 5000 and daily_steps < 7500:
        return 3
    elif daily_steps > 2500 and daily_steps < 5000:
        return 2
    elif daily_steps < 2500:
        return 1
    
def workouts_per_week_calculator(workouts_per_week):
    if 5 == workouts_per_week > 5:
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

print("Kcal and bmi counter v3 made by nothing to do!")
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
    
    input_data = f'Your name is {name} and you are a {genre}. You are {age} years old, you are tall {height}cm and your weight is {weight}kgs'
    input_data_2 = f'Your daily steps is around {daily_steps} and you do {workouts_per_week} workouts every week' 
    print(input_data + '/n ' + input_data_2)
    choose = input("That's correct? :").strip().lower().replace(" ", "")
    if "yes" in choose or "yeah" in choose or "yeh" in choose:
        bmi_value = float(bmi_calculation(int(height), int(weight)))
        if "female" in genre.lower().strip().replace(" ", ""):
            kcal_value = female_kcal(int(age), int(height), int(weight))
            TDEE = TDEE_calculator(life_style_score, kcal_value)
            message = f'Your BMI is {bmi_value:.2f} and your BMR {round(kcal_value)} per day!'
            message_2 = f'Your movement score is {life_style_score} so you have to stay around {TDEE} kcals per day!'
            print(message)
            print(message_2)
            break
        elif "male" in genre.lower().strip().replace(" ", ""):
            kcal_value = male_kcal(int(age), int(height), int(weight))
            TDEE = TDEE_calculator(life_style_score, kcal_value)
            message = f'Your BMI is {bmi_value:.2f} and your BMR {round(kcal_value)} per day!'
            message_2 = f'Your movement score is {life_style_score} so you have to stay around {TDEE} kcals per day!'
            print(message)
            print(message_2)
            break
    elif "no" in choose or "nah" in choose or "nope" in choose:
        continue
    else:
        continue

