'''
Scrivere del codice in Python per calcolare la radice quadrata 
di un numero intero e > 0 inserito da tastiera
'''

#imports
import os
import math

#funzioni
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def get_numero():
    return (int(input('Inserisci un numero : ')))

#codice principale
clear_console()
numero = get_numero()
while numero < 0:
    print('Il numero inserito è minore di 0!')
    numero = get_numero()

risultato = math.sqrt(numero)
msg = f'La radice quadrata di {numero} è {risultato}'
print(msg)