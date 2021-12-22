# Шаг 1. Загадать число +
import random
number = random.randint(1, 100)
# TODO: Version 6 +multiplayer
user_number = None
count = 0

levels = {1: 10, 2: 5, 3: 3} # difficulty level: number of attempts
level = int(input('Сhoose the difficulty level (1-3): '))
max_count = levels[level]

user_count = int(input('Enter the number of players: '))
users = []
for i in range(user_count) :
    user_name = input(f'Enter the player`s name {i+1}: ')
    users.append(user_name)

is_winner = False
winner_name = None

while not is_winner :
    count += 1
    if count > max_count:
        print('All the players lost!')
        break
    print(f'Attempt № {count}')
    # Шаг 2. Предложить пользователю угадать число
    # Suggest the user to guess the number
    for user in users:
        print (f'{user}`s move')
        user_number = int(input('Enter a number from 1 to 100: '))
        # Step 3. Comparing numbers, output of results
        if user_number == number :
            is_winner = True
            winner_name = user
            break
        elif user_number >  number :
            print('Your number is BIGGER then the one you made')
        else : #user_number <  number 
            print('Your number is LESS than the desired one')
else :
    print(f'You win, {winner_name}')

