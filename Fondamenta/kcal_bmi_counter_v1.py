#our first program is gonna calculate the calories needed 
#by the user indipendently from his Basal metabolic rate (BMR)
#that's work only for males subjects

name = input('What is your name? ')
age = int(input('How old are you ? '))
height = int(input('How tall are you in cm? '))
weight = int(input('How much do you weigh in kg? '))

#we also combine int(), str() and float() functions to input() function to get variable already converted

#You have to write "CTRL + ," and search for inline for enabling/disabling suggestions

kcal = (
        (10 * int(weight)) 
        + (6.25 * int(height)) 
        - (5*int(age)) 
        + 5
        )

height = float(height / 100)

bmi = weight / (height * height)

#we can play with conversion functions to avoid print problems but we convert the values to string only in the print statements
#to preserve their original data types

#print('Hi ' + name + '! your daily intake is approximately ' + str(kcal) + ' to maintain your weigh!')
print(f'Hi! {name} your daily intake is approximately {str(kcal)} to maintain your weigh!')
#print('Your BMI is approximately '+ str(bmi))
print(f'Your BMI is approximately {str(bmi)}')

