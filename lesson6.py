# Шаг 1. Загадать число +
import random
number = random.randint(1, 100)
# ! print (number)
#  Version 4 +limit the number of attempts
user_number = None
count = 0
max_count = 3
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

