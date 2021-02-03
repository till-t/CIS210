'''                             # FILE HEADER
Nature's Thermometer: Cricket Chirps.
CIS 210 Project 1-1 Hello-Cricket

Author: [Tyler Taormina]

Credits: [NA]

Determine the temperature based on cricket
chirps. (Farmers Almanac)
'''

def chirps_to_ctemp (ch25):     #FUNCTION HEADER
    '''(int) = float            #TYPE CONTRACT
                                #BRIEF DESCRIPTION refers to
                                #PARMS, RETURN VAL
    Return celsius temp estimated based on
    number of cricket chirps in a 25 second
    interval (ch25) - divide by 3 and add 4
    to get the celsius temerature.
                                #EXAMPLES OF USE
    >>>chirps_to_ctemp(48)
    20
    >>>chirps_to_ctemp(93)
    35.0
    >>>chirps_to_ctemp(0)
    4.0
    '''
    #replace pass with your code - don't forget to include return
    ctemp = 0
    for i in range(ch25):
        ctemp = (ch25/3) + 4
    return ctemp 

    

def chirps_to_ftemp(ch14):
    '''(int) = int

    Return fahrenheit temp estimated based on
    number of cricket chirps in a 14 second
    interval (ch14) - add 40. The estimated
    temperature is returned.

    >>>chirps_to_ftemp(0)
    40
    >>>chirps_to_ftemp(50)
    90
    '''
    #replace pass with your code - don't forget to include return
    ftemp = 0
    for x in range(ch14):
        ftemp = ch14 + 40
    return ftemp

    
    
