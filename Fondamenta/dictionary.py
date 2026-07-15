'''Paziente = {
    "nome": "Gabriele Pillitteri",
    "età": 27,
    "E' stato visitato?": True
}
Paziente["Data di nascita"] = "Oct 10 1998"
#print(Paziente.get("Data di nascita", "Oct 10 1998"))'''

Pazienti = {
    "Paziente_1": "Gabriele",
    "Paziente_2": "Giuseppe",
    "Paziente_3": "Francesco",
    "Paziente_4": "Marco"
}

Paziente = "Gabriele"
#.values() per i valori interni, .keys() per le chiavi o comunque i nomi
if Paziente in Pazienti.values():
    status = 1
else:
    status = 0

print(status)