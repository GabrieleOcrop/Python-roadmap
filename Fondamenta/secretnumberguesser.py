#modules import
import os
import random

#functions
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

#main code
#random integer number from 1 to 10
#we can also take a range between the numbers like this
#secret_numbers.random.sample(range(0, 32), 5) result is a list of 5 values from 0 to 32 with no repeats
secret_number = random.randint(0, 10)
try_counter = 0
try_limits = 5
while try_counter < try_limits:
    input_number = int(input("Try to guess the number! "))
    try_counter += 1
    if input_number == secret_number:
        print("You WON!")
        break
else:    
    print("You Lost!!")
