'''
Scrivere un codice che legga da tastiera 3 numeri interi e stampi a video 
il maggiore tra essi, il minore tra essi, la media aritmetica e la radice 
quadrata della somma (se possibile)
'''

#imports
import math
import os

#funzioni
def clear_console():

    os.system("cls" if os.name == "nt" else "clear")

def ricerca_max(a,b,c):
    if a > b:
        if a > c:
            max = a
        else:
            max = c
    else:
        if b > c:
            max = b
        else:
            max = c
    return(max)

def ricerca_min(a,b,c):
    if a < b:
        if a < c:
            min = a
        else:
            min = c
    else:
        if b < c:
            min = b
        else:
            min = c
    return(min)

def media_aritmetica (a,b,c):
    return (
        (a + b + c) / 3
    )

def radice_della_somma(a,b,c):
    return (math.sqrt(a + b + c))

#codice principale
clear_console()
a = int(input('Inserisci il primo numero intero : '))
b = int(input('Inserisci il secondo numero intero : '))
c = int(input('Inserisci il terzo numero intero : '))

val_min = ricerca_min(a,b,c)
val_max = ricerca_max(a,b,c)
media = media_aritmetica(a,b,c)
ris_radice = radice_della_somma(a,b,c)

msg = f'Il val maggiore è {val_max}, Il valore minore è {val_min}'
msg_2 = f'La media aritmetica è uguale a {media} \n e la radice della somma è uguale a {ris_radice}'

print(msg, "\n", msg_2)
