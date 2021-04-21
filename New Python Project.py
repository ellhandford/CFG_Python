         import csv

from sys import exit

field_names = ['my_score', 'opponent_score']

with open('current.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet.writeheader()

import random
import requests


def random_pet():
    pet_number = random.choice(tuple(cardnumbers))
    cardnumbers.remove(pet_number)
    # print(cardnumbers)
    url = 'http://bdddb5fbcfc8.ngrok.io/animals/{}'.format(pet_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'size': pokemon['size'],
        'fluffiness': pokemon['fluffiness'],
        'grumpiness': pokemon['grumpiness'],
        'friendliness': pokemon['friendliness'],
        'intelligence': pokemon['intelligence'],
        'mischief': pokemon['mischief'],
        'cuteness': pokemon['cuteness'],
    }


def run():
    if random_num == 1:
        choice1 = random_pet()
        choice2 = random_pet()
        choice3 = random_pet()
        print('Which pet would you like to play:')
        print('1. {}. 2. {} or 3. {}'.format(choice1['name'],
                                             choice2['name'],
                                             choice3['name']))
        poke = input('Chose 1, 2 or 3: ')
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
        print('size: {}'.format(my_pokemon['size']))
        print('fluffiness: {}'.format(my_pokemon['fluffiness']))
        print('grumpiness: {}'.format(my_pokemon['grumpiness']))
        stat_choice = input('Which stat do you want to use? (id, size, fluffiness, grumpiness) ')
        opponent_pokemon = random_pet()
        print('Your opponent chose {}'.format(opponent_pokemon['name']))
        print('Their {} is {}'.format(stat_choice, (opponent_pokemon[stat_choice])))

        print('{} vs {}'.format(my_pokemon['name'], opponent_pokemon['name']))

        my_stat = my_pokemon[stat_choice]
        opponent_stat = opponent_pokemon[stat_choice]
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

    if random_num == 2:
        choice1 = random_pet()
        choice2 = random_pet()
        choice3 = random_pet()
        print('Which pet would you like to play:')
        print('1. {}. 2. {} or 3. {}'.format(choice1['name'],
                                             choice2['name'],
                                             choice3['name']))
        poke = input('Chose 1, 2 or 3: ')
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
        print('friendliness: {}'.format(my_pokemon['friendliness']))
        print('mischief: {}'.format(my_pokemon['mischief']))
        print('cuteness: {}'.format(my_pokemon['cuteness']))
        print('intelligence: {}'.format(my_pokemon['intelligence']))

        def random_choice():
            choice_number = random.randint(1, 4)
            if choice_number == 1:
                choice = 'friendliness'
            elif choice_number == 2:
                choice = 'mischief'
            elif choice_number == 3:
                choice = 'cuteness'
            else:
                choice = 'intelligence'
            return choice

        opponent_choice = random_choice()
        print('Your opponent would like to use the stat: {}'.format(opponent_choice))

        opponent_pokemon = random_pet()
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


cardnumbers = list(range(1, 16))

number = int(input('How many rounds would you like to play: 1, 2 or 3? '))

if number == 1:
    print('Get ready for Pawfect Pets Top Trumps!')
elif number == 2:
    print('Get ready for Pawfect Pets Top Trumps!')
elif number == 3:
    print('Get ready for Pawfect Pets Top Trumps!')
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
