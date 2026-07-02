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


#main program
clear_console()

print("Kcal and bmi counter v3 made by nothing to do!")
while True:
    name = get_name()
    genre = get_genre()
    age = get_age()
    height = get_height()
    weight = get_weight()
    
    input_data = f'Your name is {name} and you are a {genre}. You are {age} years old, you are tall {height}cm and your weight is {weight}kgs'
    print(input_data)
    choose = input("That's correct? :").strip().lower().replace(" ", "")
    if "yes" in choose or "yeah" in choose or "yeh" in choose:
        bmi_value = float(bmi_calculation(int(height), int(weight)))
        if "female" in genre.lower().strip().replace(" ", ""):
            kcal_value = female_kcal(int(age), int(height), int(weight))
            message = f'Your BMI is {bmi_value:.2f} and your daily intake must be around {round(kcal_value)} per day!'
            print(message)
            break
        elif "male" in genre.lower().strip().replace(" ", ""):
            kcal_value = male_kcal(int(age), int(height), int(weight))
            message = f'Your BMI is {bmi_value:.2f} and your daily intake must be around {round(kcal_value)} per day!'
            print(message)
            break
    elif "no" in choose or "nah" in choose or "nope" in choose:
        continue
    else:
        continue

