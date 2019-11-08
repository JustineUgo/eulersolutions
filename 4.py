#Largest Prime Factor
import math

def lpf(value):
    
    odd_factors = []
    #append odd factors to odd_factor list
    for number in range(3, math.ceil(math.sqrt(value))+1):
        if number % 2 == 0:
            continue
        odd_factors.append(number)
        
    return odd_factors

    
print(lpf(int(input("What your number?: "))))
