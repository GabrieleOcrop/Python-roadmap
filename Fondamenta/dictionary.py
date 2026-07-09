Paziente = {
    "nome": "Gabriele Pillitteri",
    "età": 27,
    "E' stato visitato?": True
}
Paziente["Data di nascita"] = "Oct 10 1998"
print(Paziente.get("Data di nascita", "Oct 10 1998"))

