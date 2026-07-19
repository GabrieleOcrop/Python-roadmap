#in class non si usano underscore per separare più parole. Si usa la prima lettera maiuscola
#sono dei set che possiamo utilizzare in tutto il codice
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")



#le classi vengono usate per usare gli scheletri degli oggeti, mentre degli oggetti sono delle istanze

point1 = Point()
point1.x = 10
point1.x = 10
print(point1.x)
point1.draw()

point2 = Point()
print(point2.x)