is_hot = False
is_cold = True
# This function uses the global variables defined above.
# Since it doesn't have parameters, it automatically reads
# the values of is_hot and is_cold.
# we can also add local parameters like this def(weather(is_hot, is cold))
def weather():
    #condition to verify
    if is_hot:
        #if the first condition is met
        print("Make sure to drink a lot of water")
    elif is_cold:
        #another condition to verify
        #if the second condition is met
        print("Drink normally it's a cold day!")
    else:
        #otherwise do this
        print("Don't worry! enjoy your day")
#to execute this requires the results like this weather(true, false)
weather()