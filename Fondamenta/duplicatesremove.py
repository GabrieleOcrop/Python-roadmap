'''
write a program to remove the duplicates in a list
'''

import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


clear_console()
numbers = [5, 2, 6, 1, 6, 25, 5, 13, 3]
duplicate_free = numbers.copy()

for number in duplicate_free:
    if duplicate_free.count(number) >= 2:
        duplicate_free.remove(number)

print(numbers)
print("\n")
print(duplicate_free)


'''soluzione moss
    for number in numbers:
        if number not in uniques:
            uniques.append(number)
print(uniques)
'''