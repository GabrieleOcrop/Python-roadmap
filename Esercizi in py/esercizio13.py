'''
Scrivere del codice in Python per chiedere all’utente di inserire 
una base b e un esponente e per poi calcolare b elevato a e
'''
#imports
import os

#funzioni

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def ottieni_base():
    return(input('Inserisci la base : '))

def ottieni_esponente():
    return(input("Inserisci l'esponente : "))

def calcola_elevazione(base, esponente):
    return (
        base * esponente
    )

#codice_principale

clear_console()

base = int(ottieni_base())
esponente = int(ottieni_esponente())
risultato = calcola_elevazione(base, esponente)
msg = f"B^e = {risultato}"
print(msg)