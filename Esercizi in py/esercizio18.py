j'''
Scrivere un codice Python che legga da tastiera un valore nell'intervallo [1,12]  ̶ 
corrispondente ad un mese   ̶ e stampi la stagione relativa al mese inserito.
Il codice deve cercare di intercettare possibili situazioni di errore dovute a input fuori 
dall’intervallo predefinito.
'''

#imports
import os
#funzioni
def clear_console():
    os.system("cls" if os.name == "nt" else clear)

#main program
clear_console()
valore_inserito = int(input("Inserisci un valore tra 1 e 12 : "))

if valore_inserito is chr:
    print("Valore non valido!")
    quit()elif valore_inserito < 1 and valore_inserito > 12:
    print("Valore non valido")
elif valore_inserito == 12 and valore_inserito >= 1 and valore_inserito <= 2: 
    print("Inverno")
elif valore_inserito >= 3 and valore_inserito <= 5:
    print("Primavera")
elif valore_inserito >= 6 and valore_inserito <= 8:
    print("Estate")
elif valore_inserito >= 9 and valore_inserito <= 11:
    print("Autunno")
    
