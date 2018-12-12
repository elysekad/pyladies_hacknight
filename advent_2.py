import numpy as np
advent_1 = np.loadtxt('C:/python/advent_1.csv')

numbers = []
m=0
numbers.append(m)

while True:
    for item in advent_1: 
        m+=item
        if m in numbers:
            print(m)
            exit()
        else:
            numbers.append(m)

        
    
        
            

