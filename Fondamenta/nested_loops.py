#main loop
for x in range(4):  
    #inner loop depending by the first, for the first loop in x there are 3 loops in y
    #x = 0; y = 0; y = 1; y = 2; y = 3
    for y in range(3):
        print(f'({x} , {y})')
