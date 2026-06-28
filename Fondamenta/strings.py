#we must use the double quotes to add single quote to string
#the same works for adding the double quotes by adding single quotes
saluto = "Hi! i'm gabriele"
print(saluto)
leone = 'I do like "75lbs bicep curl" for 5 sets'
print(leone)
message = '''
    i'm gabriele
    imagine your trip is like an diary
    the only thing you have to do
    is add more pages
    and it works :|
'''
print(message)

#we can also imagine strings like arrays
#this will print the second character at your right
print(saluto[-2])
#this will return the charaters from index 0 to index 8
print(saluto[0:8])
#this will let print all the characters by 3 to the last
print(saluto[3:])
#this will print from 0 to 4, if that's empty the coder will read as 0 
print(saluto[:4])

name = 'gabriele'
print(name[1:-1])