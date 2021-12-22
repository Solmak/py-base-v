# Шаг 1. Загадать число +
import random

number = random.randint(1, 100)
# ! print (number)

#  Version 2
while user_number != number :
    # Шаг 2. Предложить пользователю угадать число
    # Suggest the user to guess the number
    user_number = int(input('Enter a number from 1 to 100: '))
    # ! print (user_number)
    # Step 3. Comparing numbers, output of results
    if user_number >  number :
        print('Your number is bigger then the one you made')
    elif user_number <  number :
        print('Your number is less than the desired one')

print('You win!')
