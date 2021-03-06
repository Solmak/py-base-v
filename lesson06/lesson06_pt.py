"""
В этой игре человек загадывает число, а компьютер пытается его угадать.
В начале игры человек загадывает число от 1 до 100 в уме или записывает
его на листок бумаги. 
Компьютер начинает его отгадывать предлагая игроку варианты чисел. 
Если компьютер угадал число, игрок выбирает “победа”. 
Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”. 
Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”.
Игра продолжается до тех пор пока компьютер не отгадает число.

"""
import random

# Фразы компьютера
phrases = (
    'Ну давай попробуем {}\n',
    'Может это {}?\n',
    'Возможно {}?\n',
    'Я уверен, что это {}!\n'
)
print('Загадайте число от 1 до 100\nЯ буду называть вам числа\nЕсли я угадаю - введите =\nЕсли моё число больше - >\nЕсли моё число меньше - <\nА кто будет жульничать, того будем бить по морде!\nПо наглой рыжей морде!')
# Для проверки ввода пользователя
user_answers = ('=','<','>')
# Начальный диапазон
range_begin = 1
range_end = 100

# Основной цикл
user_input = None
count = 0
while user_input != '=' :
    count += 1
    user_input = None
    #начало конец Не стал делать метод половин - очень однообразно выходит
    number = random.randint(range_begin, range_end)  
    while not user_input in user_answers:
        user_input = input(phrases[random.randint(0, len(phrases) - 1)].format(number)) # учим разговаривать
        if not user_input in user_answers: # исключительно для пояснения неверных действий
            print('Может тебе непонятьно? Можно только "=", ">" или "<"')
    # сужаем диапазон 
    if user_input == '>':
        if number <= range_begin:
            print('Рыжая морда! Вы шулер! Я с вами не играю!')
            break
        range_end = number - 1
    elif user_input == '<':
        if number >= range_end:
            print('Подлый лис! Опять шельмуешь?! Я с тобой больше не играю!')
            break
        range_begin = number + 1

else:
    print(f'Ха! Я тебя сделал всего за {count} попыток!')




