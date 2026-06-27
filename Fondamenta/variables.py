#that's the file where we define all the variables that we can and will use in the projects
nome = "Gabriele"
cognome = "Pillitteri"
età = 27
mansione = "Assistente di cantiere"
#now we defined 4 variables wich are nome, cognome, età and mansione
#the string must be in quotes, either single or double quotes, while the integer must not be in quotes
#3 of this are strings and 1 is an integerù
print(nome)
print(cognome)
print(età)
#we can also use accented characters in the variable names, but 
#we must not use them for good practice, it can create problems
print(mansione)

età = 45

print(età)
#py execute the code from the top to the bottom, 
#so if we change the value of a variable, the new value
#will be used and not the old one
#a number without quotes is an integer, while a number with quotes is a floating value

rating = 4.9

print(rating)

#we can also define a variable name using underscores 

is_good = False

#that's a boolean variable, it can be either True or False 
#we can combine in a print statement a string and a variable, just by putting the string in quotes and the variable without quotes after a comma

print("It is good?", is_good)