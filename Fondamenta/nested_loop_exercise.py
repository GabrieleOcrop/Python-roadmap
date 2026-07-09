numbers = [5, 2, 5, 2, 2]
'''for index in numbers:
    print_x = 0
    for number in enumerate(numbers):
        while print_x != number:
            print('x')
            print_x += 1
            '''
#print(list(enumerate(numbers)))
#[index, value]
'''for number in numbers:
    print_x = 0
    while print_x < number:
        print_x += 1
        print('x', end="")
    print()
'''
'''
mosh solution

for x_count in numbers:
    print('x' * x_count)
    we can multiply a string to a number to repeat it
'''

#mosh shows with inner loops
#for the x's i have to change output += with 'x' char
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += f'{x_count}'
    print(output)