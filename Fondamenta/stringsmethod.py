course = 'Python for Dummies'
# it gives the length of the string
# we can use it to limit user input
# it can be used in many applications
print(len(course))
# .upper() and .lower() return a new string
# without modifying the original one
print(course.upper())
print(course)
print(course.lower())
#it returns the index of the first occurrence
#of a character or substring 
#if there isn't any occurrence, it will give -1
print(course.find('for'))
# replace() replaces every occurrence
# of a character or substring
message = "I'm ugly as fuck"
print(message.replace('fuck' , '****'))
print(message.replace('f', 'd'))
# "in" returns True if a substring exists
# otherwise it returns False
print('fuck' in message)
print('duck' in message)