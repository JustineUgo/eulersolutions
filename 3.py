#Largest Prime Factor
import math

def lpf(value):
    
    square_root_of_uservalue = math.ceil(math.sqrt(value)) + 1
    
    #if factor of value
    for possible_factor in range(square_root_of_uservalue, 3, -1):
        if value % possible_factor == 0 and possible_factor%2 != 0: #if is a factor of value and not even(not prime, if even)
            
            #Returns largest prime factor of value
            square_root_of_possible_factor = math.ceil(math.sqrt(possible_factor)) + 1
            if all([possible_factor%integer!=0 for integer in range(3, square_root_of_possible_factor, 2)]):
                return possible_factor
        



    
print(lpf(int(input("What your number?: "))))

