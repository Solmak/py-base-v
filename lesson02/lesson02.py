""" print('Hello, world!')

# Определение типа переменной
person_name = 'Max'
print(type(person_name))

age = 31
print(type(age))

period = 3.2
print(type(period))

is_good = True
print(type(is_good))

person = None
print(type(person))

# Приведение типов
birthday_year = '1988'
print(type(person))

period = 20
print(type(period))

# ! Если сделаем так age = birthday_year + period , получим ошибку
# int() преобразовывает в целое
# str() преобразовывает в строку
age = int(birthday_year) + period
print(age)
some_str = birthday_year + str(period)
print(some_str)

# вывод переменных через запятую
name = 'Вася'
age = 2
print(name, age)

# вывод переменных через заданый сепаратор sep='разделитель' вместо пробела
print(name, age, sep='РазделителЬ')

# задание конца строки вместо \n end='вместо конца строки' 
print(name, end='вместо конца строки')
print(age)
# выведет Васявместо конца строки2

# input() - always return str 
result = input()
print(result)
result = input('Введите: ')
print('Вы ввели: '+result)

#_  // - целая часть от деления //
#   % - остаток от деления
#_  ** -  возведение в степень

# Оператор if
age = int(input('Введите свой возраст: '))
if  age < 18:
    print('Доступ заперщён!')
elif age == 18:
    print('Вам ровно 18!')
    print('И что с вами делать?!')
else:
    print('Доступ разрешен!')
    if age % 5 == 0:
        print('Поздравляем! У вас юбилей!')


print('Что-то')
print('Конец')
 
# ** Угадай число
number = 65
value = int(input('Введите число: '))
if value == number:
    print('Угадали!')
else:
    print('Не угадали!')
    if value > number:
        print('Это слишком много!')
    else:
        print('Это слишком мало!')

name = input('Кто создатель Python? ')
while name != 'Гвидо':
    print('Не верно!')
    name = input('Кто создатель Python? ')

print('Верно!')

# Вывод чисел от 0 до 100
number = 0;
while number <= 100:
    print(number)
# *    number = number +1
    number += 1

# Вывод чисел от 0 до n, которое вводит пользователь
number = 0
maxNumber = int(input('Введите число от 0 до 100: '))
while number <= maxNumber:
    print(number)
    number += 1
"""
# Вывод четных чисел от 0 до n, которое вводит пользователь
# @param number lk;lk;lk
number = 0
maxNumber = int(input('Введите число от 0 до 100: '))
while number <= maxNumber:
    if number % 2 == 0:
        print(number)
    if number == 33:
        break
    number += 1
# Блок else выполняется только ТОГДА, когда мы выходим из цикла по условию
else:
    print('end')
