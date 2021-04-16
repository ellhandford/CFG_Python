import csv

from sys import exit

field_names = ['my_score', 'opponent_score']

with open('current.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet.writeheader()

import random
import requests

def random_pokemon():
    pokemon_number = random.choice(tuple(cardnumbers))
    cardnumbers.remove(pokemon_number)
    #print(cardnumbers)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }


def run():
    if random_num == 1:
        choice1 = random_pokemon()
        choice2 = random_pokemon()
        choice3 = random_pokemon()
        poke = input('Which pokemon would you like to play: 1. {}. 2. {} or 3. {} (chose 1, 2 or 3): '.
                     format(choice1['name'],
                            choice2['name'],
                            choice3['name']))
        if poke == '1' :
            my_pokemon = choice1
        elif poke == '2' :
            my_pokemon = choice2
        elif poke == '3':
            my_pokemon = choice3
        else:
            print("You didn't draw that card!")
            return

        print('You chose {}'.format(my_pokemon['name']))
        print('id: {}'.format(my_pokemon['id']))
        print('height: {}'.format(my_pokemon['height']))
        print('weight: {}'.format(my_pokemon['weight']))
        stat_choice = input('Which stat do you want to use? (id, height, weight) ')
        opponent_pokemon = random_pokemon()
        print('The opponent chose {}'.format(opponent_pokemon['name']))
        print('Their {} is {}'.format(stat_choice, (opponent_pokemon[stat_choice])))
        my_stat = my_pokemon[stat_choice]
        opponent_stat = opponent_pokemon[stat_choice]
        if my_stat > opponent_stat:
            print('You Win!')
            import csv
            field_names = ['my_score', 'opponent_score']
            data = [
                {'my_score': 1, 'opponent_score':0},
            ]
            with open('current.csv', 'a') as csv_file:
                spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
                spreadsheet.writerows(data)
        elif my_stat < opponent_stat:
            print('You Lose!')
            import csv
            field_names = ['my_score', 'opponent_score']
            data = [
                {'my_score': 0, 'opponent_score': 1},
            ]
            with open('current.csv', 'a') as csv_file:
                spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
                spreadsheet.writerows(data)
        else:
            print('Draw!')

    if random_num == 2:
        choice1 = random_pokemon()
        choice2 = random_pokemon()
        choice3 = random_pokemon()
        poke = input('Which pokemon would you like to play: 1. {}. 2. {} or 3. {} (chose 1, 2 or 3): '.
                     format(choice1['name'],
                            choice2['name'],
                            choice3['name']))
        if poke == '1':
            my_pokemon = choice1
        elif poke == '2':
            my_pokemon = choice2
        elif poke == '3':
            my_pokemon = choice3
        else:
            print("You didn't draw that card!")
            return


        print('You chose {}'.format(my_pokemon['name']))
        print('id: {}'.format(my_pokemon['id']))
        print('height: {}'.format(my_pokemon['height']))
        print('weight: {}'.format(my_pokemon['weight']))
        def random_choice():
            choice_number = random.randint(1, 3)
            if choice_number == 1:
                choice = 'id'
            elif choice_number == 2:
                choice = 'height'
            else:
                choice = 'weight'
            return choice

        opponent_choice = random_choice()
        print('Your opponent would like to use the stat: {}'.format(opponent_choice))

        opponent_pokemon = random_pokemon()
        print('The opponent chose {}'.format(opponent_pokemon['name']))
        print('Their {} is {}'.format(opponent_choice, (opponent_pokemon[opponent_choice])))

        my_stat = my_pokemon[opponent_choice]
        opponent_stat = opponent_pokemon[opponent_choice]

        if my_stat > opponent_stat:
            print('You Win!')
            import csv
            field_names = ['my_score', 'opponent_score']
            data = [
                {'my_score': 1, 'opponent_score': 0},
            ]
            with open('current.csv', 'a') as csv_file:
                spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
                spreadsheet.writerows(data)
        elif my_stat < opponent_stat:
            print('You Lose!')
            import csv
            field_names = ['my_score', 'opponent_score']
            data = [
                {'my_score': 0, 'opponent_score': 1},
            ]
            with open('current.csv', 'a') as csv_file:
                spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
                spreadsheet.writerows(data)
        else:
            print('Draw!')

cardnumbers = list(range(1,16))

number = int(input('How many rounds would you like to play: 1, 2 or 3?'))

if number == 1:
    print('Get ready for Pokemon Top Trumps!')
elif number == 2:
    print('Get ready for Pokemon Top Trumps!')
elif number == 3:
    print('Get ready for Pokemon Top Trumps!')
else:
    print("Oh no, you don't have enough cards for {} rounds, try again!".format(number))
    exit()

Count = 0

for i in range(number):
    Count = Count + 1
    print(' ')
    print('Round {}: '.format(Count))
    random_num = random.randint(1, 2)
    run()

with open('current.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    my_score = []

    for row in spreadsheet:
        sco = row['my_score']
        my_score.append(sco)


with open('current.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    opponent_score = []

    for row in spreadsheet:
        sco = row['opponent_score']
        opponent_score.append(sco)

my_total = 0

opponent_total = 0

for ele in range(0, len(my_score)):
    my_total = my_total + int(my_score[ele])

for ele in range(0, len(opponent_score)):
    opponent_total = opponent_total + int(opponent_score[ele])



print(' ')
print('And the final results are in...')
print('The score is {}:{}'.format(my_total, opponent_total))
if my_total > opponent_total:
    print('You Win!')
elif my_total < opponent_total:
    print('You Lose!')
else:
    print('Draw!')

name = input('Please write your name for the scoreboard: ')
score = (my_total - opponent_total)
print('Your leaderboard score is: {}'.format(score))

import csv

field_names = ['name', 'score']

data = [
    {'name': name, 'score': int(score)},
]

with open('highscore.csv', 'a') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

    spreadsheet.writerows(data)

with open('highscore.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    scores = []

    for row in spreadsheet:
        sco = row['score']
        scores.append(sco)


highest_score = max(scores)
print('')
print('The current highscore is : {}'.format(highest_score))
