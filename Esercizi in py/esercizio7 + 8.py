'''
Esercizio 7
Scrivere del codice Python per richiedere all’utente
di inserire da tastiera il proprio nome.
Una volta recuperato il nome, esso dovrà essere 
stampato a video.

Esercizio 8
Aggiungere la quantità di caratteri presenti sul nome
'''

nome = input('Come ti chiami? :')
qt_caratteri = len(nome)
msg = f'Il nome inserito è {nome} ed è composto da {qt_caratteri} lettere'
print(msg)