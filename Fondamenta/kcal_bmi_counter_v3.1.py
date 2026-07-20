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

#Functions to get values

def ask_name():
    name = input("What's your name? :").strip()
    return name

def ask_genre():
    genre = input("Are you male or female? :")
    return genre

def ask_age():
    age = input("How old are you? :")
    return age


def ask_height():
    height = input("How tall are you? Be sure that's in centimeters! :")
    return height

def ask_weight():
    weight = input("How much do you weight? Be sure that's in kilograms! :")
    return weight

def ask_workouts_per_week():
    workouts_per_week = input("How many workouts do you do per week? :")
    return workouts_per_week

def ask_daily_steps():
        daily_steps = input("How many steps do you usually take each day? :")
        return daily_steps

#Functions to validate!

def validate_name(name):
    if not name:
        raise ValueError("Name cannot be empty!")
    elif (len(name) < 3) or (len(name) > 16):
        raise ValueError("Name seems to be invalid!")
    elif any(char.isdigit() for char in name):
        raise ValueError("Name doesn't accept numbers!")

def validate_genre(genre):
    if not genre:
        raise ValueError("Genre cannot be empty!")
    elif genre not in allowed_genre_responses:
        raise ValueError("Genre accepts only Male and Female!")

def validate_age(age):
    if not age:
        raise ValueError("Age cannot be empty!")
    elif not age.isdigit():
        raise ValueError("Age cannot accepts characters!")
    elif (int(age) > 120):
        raise ValueError("Age input seems to be too high!")

def validate_height(height):
    if not height:
        raise ValueError("Height cannot be empty!")
    elif not height.replace(".", "", 1).isdigit():
        raise ValueError("Height value seems to be invalid")

def validate_weight(weight):
    if not weight:
        raise ValueError("Weight cannot be empty!")
    elif not weight.replace(".", "", 1).isdigit():
        raise ValueError("Weight value seems to be invalid")

def validate_workouts_per_week(workouts_per_week):
    if not workouts_per_week:
        raise Exception("Your workouts number must have a number! 0 is just fine")
    elif not workouts_per_week.isdigit():
        raise Exception("Workouts per week accepts only numbers!")
    elif int(workouts_per_week) > 7:
        raise Exception("That version counts only 1 workout per day! Revise with 7")

def validate_daily_steps(daily_steps):
    if not daily_steps:
        raise Exception("Daily Steps cannot be empty!")
    elif not daily_steps.isdigit():
        raise Exception("Daily steps accept only numbers!")
    

#functions to get the value!

def get_name():
    while True:    
        try:
            name = ask_name()
            validate_name(name)
            return name
        except ValueError as error:
            print(f'An error has happened! => {error}')

def get_genre():
    while True:
        try:
            genre = ask_genre()
            validate_genre(genre)
            return genre
        except ValueError as error:
            print(f'An error has happened! => {error}|')

def get_age():
    while True:
        try:
            age = ask_age()
            validate_age(age)
            return int(age)
        except ValueError as error:
            print(f'An error has happened => {error}')

def get_height():
    while True:
        try:
            height = ask_height()
            validate_height(height)
            return float(height)
        except ValueError as error:
            print(f'An error has happened => {error}')

def get_weight():
    while True:
        try:
            weight = ask_weight()
            validate_weight(weight)
            return float(weight)
        except ValueError as error:
            print(f'An error has happened => {error}')

def get_workouts_per_week():
    while True:
        try:
            workouts_per_week = ask_workouts_per_week()  
            validate_workouts_per_week(workouts_per_week)
            return int(workouts_per_week)    
        except ValueError as error:
            print(f'An error has happened => {error}')

def get_daily_steps():
    while True:
        try:
            daily_steps = ask_daily_steps()
            validate_daily_steps(daily_steps)
            return int(daily_steps)
        except ValueError as error:
            print(f'An error has happened => {error}')      
        
#calculations

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

print("Kcal, bmi and TDEE counter v3.1 made by nothing to do!")

name = get_name()
genre = get_genre() 
age = get_age()
height = get_height()
weight = get_weight()
daily_steps = get_daily_steps()
workouts_per_week = get_workouts_per_week()       

daily_steps_score = daily_steps_score_calculator(daily_steps)
workouts_per_week_score = workouts_per_week_calculator(workouts_per_week)
life_style_score = score_life_style_calculator(daily_steps_score, workouts_per_week_score)
input_data = f'Your name is {name} and you are a {genre}. You are {age} years old, you are tall {height}cm and your weight is {weight}kgs. \n Your daily steps is around {daily_steps} and you do {workouts_per_week} workouts every week'
print(input_data) 
bmi_value = bmi_calculation(height,weight)
if genre.strip().lower() == "female" or genre.strip().lower() == "f":
    kcal_value = female_kcal(age, height, weight)
    TDEE = TDEE_calculator(life_style_score, kcal_value)
    message = f'Your BMI is {bmi_value:.2f} and your BMR {round(kcal_value)} per day! \n Your life_style score is {life_style_score} so you have to stay around {round(TDEE)} kcals per day!'
    print(message)
elif genre.strip().lower() == "male" or genre.strip().lower() == "m":
    kcal_value = male_kcal(age, height, weight)
    TDEE = TDEE_calculator(life_style_score, kcal_value)
    message = f'Your BMI is {bmi_value:.2f} and your BMR {round(kcal_value)} per day! \n Your movement score is {life_style_score} so you have to stay around {round(TDEE)} kcals per day!'
    print(message)
