import os 
import math

#functions
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

#def dumb_choose_analysis(user_input):


def lbs_to_kgs(input_weight):
    return input_weight * 0.4536

def kgs_to_lbs(input_weight):
    return input_weight * 2.2050

#main program
clear_console()
print("Weight Converter v1.0")
input_weight=input('Insert the value do you want to convert : ')
#cleaning the input for more like AI input
user_input=input('What do you want to do? :').lower().strip().replace(" ", "")

#verify the order into the string input
if "lbstokgs" in user_input or "lbtokg" in user_input or "lbtokgs" in user_input or "lbstokg" in user_input:
    converted_weight=lbs_to_kgs(float(input_weight))
    print(f'The {input_weight}lbs are {converted_weight}kgs ')
elif "kgstolbs" in user_input or "kgtolb" in user_input or "kgstolb" in user_input or "kgtolbs" in user_input:
    converted_weight=kgs_to_lbs(float(input_weight))
    print(f'The {input_weight}kgs are {converted_weight}lbs ')
else:
    print("I'm not sure about that!")
    quit()
