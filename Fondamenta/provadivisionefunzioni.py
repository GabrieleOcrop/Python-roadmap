def ask_name():
    name = input("What's your name? :").strip()
    return name

def validate_name(name):
    if not name:
        raise ValueError("Name cannot be empty!")
    elif (len(name) < 3) or (len(name) > 16):
        raise ValueError("Name seems to be invalid!")
    elif any(char.isdigit() for char in name):
        raise ValueError("Name doesn't accept numbers!")

def get_name():
    while True:    
        try:
            name = ask_name()
            validate_name(name)
            return name
        except ValueError as error:
            print(f'An error has happened! :{error}')
        

name = get_name()
print(name)