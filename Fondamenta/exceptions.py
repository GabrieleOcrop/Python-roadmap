try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
#what happen if the programm meet an error in value types
except ValueError:
    print('Invalid input')
except ZeroDivisionError:
    print('Age cannot be 0')