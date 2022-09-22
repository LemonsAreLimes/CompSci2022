# CHALLENGE 3

# Create a program that prints out the name of your favourite cities
# Use at least ONE function – named favourite_city
# favourite_city should have ONE parameter: “name”
# Call () favourite_city function at least 3 times
# The output should include “One of my favourite cities is”…
# Add a screenshot of your source code AND your terminal win

from random import randint

def favorate_city(name=None):
    if name == None: return False
    return f'one of my favorate cities is: {name}'

cities_list = [
    'Oslo',
    'Stockholm',
    'Amsterdam',
    'Berlin',
    'Paris',
    'Madrid',
    'Kyiv',
    'Minsk',
    'Tallinin',
    'moscow',
    'edmonton'
]
    
for i in range(3):

    chosen_city = cities_list[randint(1, len(cities_list)-1)]
    text = favorate_city(chosen_city)

    if text != False:
        print(text)
    else:
        print('something has went terribly wrong!')