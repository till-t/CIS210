'''
CIS 210
Project 3-1: Fizzbuzz

Author: Tyler Taormina

Credits: N/A

'''

def fb(n):
    '''fizz buzz function that looks for numbers 
    divisible by 3, 5, or 3 and 5
    '''
    
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print ('fizzbuzz')
            continue 

            
        elif i % 3 == 0:
            print ('fizz')
            continue 

        
        elif i % 5 == 0:
            print ('buzz')
            continue 

        
        else:
            print (i)
            continue
            
    
        return None 
