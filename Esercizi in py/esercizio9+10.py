'''
Scrivere delle istruzioni Python in grado di prendere in ingresso 
da tastiera un intero x e stampare a video il valore -x
'''

numero = int(input('Inserisci un numero! :'))
if(numero < 0):
    msg = f'Hai inserito un numero negativo e il suo val assoluto è {abs(numero)}'
    print(msg)
else:
    msg = f'Hai inserito un numero positivo e il suo val negativo è -{numero}'
    print(msg)