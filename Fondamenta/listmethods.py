numbers = [5, 2, 13, 5, 7]
#per aggiungere oggetti alla fine della lista
#numbers.append(29)

#Per aggiungere oggetti in una determinata posizione della lista
#Il primo valore accetta l'indice, mentre il secondo accetta il valore vero e proprio
#numbers.insert(0, 35)

#Ci permette di rimuovere un valore e accetta come parametro il valore che vogliamo rimuovere
#numbers.remove(13)

#Ci permette di pulire tutto l'array
#numbers.clear()

#Ci permette di rimuovere l'ultimo elemento di un array
#numbers.pop()

#il metodo index restituisce l'indice della prima coincidenza contenuta nella lista, ricerca di valori molto base
#print(numbers.index(5))
#print(numbers)

#Questo è un'altro metodo di ricerca all'interno di una lista e ci restituisce un valore booleano Vero o Falso
#A differenza di index se manca non ci restituisce un errore
#print(5 in numbers)

#Il metodo count conta quante volte è presente un determinato elemento all'interno della lista
#print(numbers.count(5))

#il metodo sort ci permette di riordinare la lista con ordine crescente
#numbers.sort()
#il metodo reverse ci permette di invertire l'ordine della lista, e in questo caso otteniamo un ordinamento decrescente
#numbers.reverse()

#il metodo copy ci permette di copiare l'intera lista all'interno di un'altra lista
#utile per effettuare delle modifiche alla lista mantenendo l'originale
numbers_2 = numbers.copy()
print(numbers_2)