joke_dataset = [

    ['Did you hear about the mathematician who’s afraid of negative numbers?', 'He’ll stop at nothing to avoid them.'],
    ['Hear about the new restaurant called Karma?', 'There’s no menu: You get what you deserve.'],
    ['Did you hear about the actor who fell through the floorboards?', 'He was just going through a stage.'],

]

# these jokes are stolen from https://www.rd.com/list/short-jokes/
# i am not very origonal with this type of stuff lmao

from random import randint
joke_id = randint(0, len(joke_dataset))
print(joke_dataset[joke_id][0])

while True:
    input('you respond with: ')
    print(joke_dataset[joke_id][1]); exit()
