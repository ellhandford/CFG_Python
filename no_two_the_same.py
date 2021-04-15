#%%
import random
import numpy as np

cards = int(input('How many cards would you like to draw? '))

print('Drawing {} cards....'.format(cards))

a = 1
b = 14

random_cards = random.sample(range(a, b+1), cards)

for card in (random_cards):
    print('You drew card {}'.format(card))

player_card =int(input('Which card would you like to play?'))

if player_card not in random_cards:
    print('Not valid! You did not draw that card!')
else:
    print('Need to integrate with base code :)')

# %%
