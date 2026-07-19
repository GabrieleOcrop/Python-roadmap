class Guy:

    def __init__(self, name):
        self.name = name
    
    def ask_name():
        name = input("What's your name? :")
        return name
    
    def talk(self):
        print(f'Hi {self.name} welcome!')




guy_1 = Guy(Guy.ask_name())
guy_1.talk()

guy_2 = Guy(Guy.ask_name())
guy_2.talk()

'''class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi! {self.name} welcome!')

john = Person("John smith")
john.talk()

bob = Person("Bob aggiusta tutto")
bob.talk()'''
