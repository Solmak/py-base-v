# Шаг 1. Загадать число +
import random
number = random.randint(1, 100)
# ! print (number)
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
# ! 
print(users)

while user_number != number :
    count += 1
    if count > max_count:
        print('You`ve lost!')
        break
    print(f'Attempt № {count}')
    # Шаг 2. Предложить пользователю угадать число
    # Suggest the user to guess the number
    user_number = int(input('Enter a number from 1 to 100: '))
    # ! print (user_number)
    # Step 3. Comparing numbers, output of results
    if user_number >  number :
        print('Your number is BIGGER then the one you made')
    elif user_number <  number :
        print('Your number is LESS than the desired one')
else :
    print('You win!')

