import os

def clear_console():
    os.system("cls" if os.name=="nt" else "clear")



clear_console()

Numbers = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero"
}

phone_number = input("Insert your phone number")
output = ""
for number in phone_number:
    output += Numbers.get(number, "!") + " "
    
print(output)