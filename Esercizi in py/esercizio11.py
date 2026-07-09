'''Si chieda all’utente di inserire due valori reali (di tipo float) x e y,
stampando il valore (x+y)/(x-y)'''

#funzioni

def prendi_valore():
    valore = input('Inserisci un valore con virgola! :')
    return valore

def calcola(valore1,valore2):
    return (
        (valore1 + valore2) 
        / 
        (valore1 - valore2)
    )

#codice principale

valore1 = float(prendi_valore())
valore2 = float(prendi_valore())

risultato = calcola(valore1,valore2)
print(risultato)
