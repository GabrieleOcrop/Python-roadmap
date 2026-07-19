class Point:
    #creazione di un oggetto con un costruttore
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(10, 20)
print(point.x)