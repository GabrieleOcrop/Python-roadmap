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
for number in numbers:
    print_x = 0
    while print_x < number:
        print_x += 1
        print('x', end="")
    print()
