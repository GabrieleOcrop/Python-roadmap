import os

def clear_console():
    os.system("cls" if os.name=="nt" else "clear")

clear_console()

emojis = {
    ":)" : "😊",
    ":(" : "☹️",
    ":*" : "😘",
}

message = input(": ")
splitted_message = message.split(' ')
output = " "

for splitted in splitted_message:
    output += emojis.get(splitted, splitted) + " "

print(output)
