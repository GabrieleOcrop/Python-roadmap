birth_year = input ('What year you were born? ')
#that's our first expression, that calculates the age of the user
#but this will not work because we are trying to subtract a string from an interger
birth_year = int(birth_year)
#int() function is used to convert a string into an interger
#now we can use the birth_year variable in our expression
#float() is another function to convert into an floating
#bool() is another function to convert into a boolean
age = 2026 - birth_year
choosen_name = input('What name you want to be called? ')
print(type(choosen_name))
#type() is a function that return the type of the variable,
#in this case it will return a string

print(choosen_name + ' is ' + str(age) + ' years old ')

#str() function in used to convert an number into a string

