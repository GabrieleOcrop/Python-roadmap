import os

#functions

#for cleaning console 
def clear_console():
    # 'cls' is for Windows, 'clear' is for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')


def verify(choose):
    if choose == "yes":
        print()
    else:
        quit()

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

print("Kcal and bmi counter v2 made by nothing to do!")
name = input("What's your name? :")
genre = input("Are you male or female? :").strip().lower()
age = input("How old are you? :")
height = input("How tall are you(cm)? :")
weight = input("How much do you weight(kgs)? :")
clear_console()

input_data = f'Your name is {name} and you are a {genre}. You are {age} years old, you are tall {height}cm and your weight is {weight}kgs'
print(input_data)
choose = input("That's correct?(yes/no) :").strip().lower()
verify(choose)

bmi_value = float(bmi_calculation(int(height), int(weight)))
if genre=="male":
    kcal_value = male_kcal(int(age),int(height),int(weight))
elif genre=="female":
    kcal_value = female_kcal(int(age), int(height), int(weight))
else:
    print("STOP!")
    quit()
    

clear_console()

message = f'Your BMI is {bmi_value:.2f} and your daily intake must be around {round(kcal_value)} per day!'
print(message)



