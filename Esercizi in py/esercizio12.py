'''
Scrivere del codice in Python per calcolare il numero delle ore 
corrispondenti all’età di una persona (espressa in anni)
In particolare, il codice deve permettere di: 
1. Richiedere all’utente di inserire la propria età in anni
2. Stampare a video il numero di ore corrispondenti
Si assuma che valga sempre 1 anno = 365 giorni
'''

#funzioni

def ottienieta():
    return(input('Quanti anni hai? :'))

def calcola_ore(eta):
    return(
        eta * 365 * 24 
        )

#codice principale

eta = int(ottienieta())
eta_in_ore = calcola_ore(eta)
msg = f'Hai {eta} anni e in ore corrisponde a circa {eta_in_ore}'
print(msg)