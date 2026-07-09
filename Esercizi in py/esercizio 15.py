'''
Scrivere un codice in Python che legga in input da tastiera le
coordinate di 2 punti nel piano cartesiano(x1,y1) e (x2,y2),
calcoli la loro distanza Euclidea e la stampi a video
'''

#imports
import os
import math
#funzioni
def clear_console():
    os.system("cls" if os.name=='nt' else 'clear')

def calcola_distanza_euclidea(x1,x2,y1,y2):
    return(
        math.sqrt(
            math.pow((x2-x1),2)
            +
            math.pow((y2-y1),2)
        )
    )

#programma principale
clear_console()
x1 = int(input('Inserisci x1 : '))
y1 = int(input('Inserisci y1 : '))
msg1 = f'Primo punto inserito => ({x1},{y1})'
print(msg1)
x2 = int(input('Inserisci x2 : '))
y2 = int(input('Inserisci y2 : '))
msg2 = f'Secondo punto inserito => ({x2},{y2})'
print(msg2)
risultato = calcola_distanza_euclidea(x1,x2,y1,y2)
msg_risultato = f'Distanza euclidea di ({x1},{y1}) e ({x2},{y2}) = {risultato}'
print(msg_risultato)