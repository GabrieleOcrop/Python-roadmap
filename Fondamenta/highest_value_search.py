values = [1, 4, 87, 14, 28, 99, 0.001, 15]
highest_value = 0
for value in values:
    if highest_value < value:
        highest_value = value
print(highest_value)