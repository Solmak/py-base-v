""" # Урок 8. Функции
# ? функции без имени?

# abs - модуль числа
print(abs(-7))

# min, max - минимальное, максимальное значение последовательности
numbers = [5,12,53,78,23,41,2,16]
print(max(numbers))
print(min(numbers))

# round - округление
print(round(23.45264, 2))

# sum - сумма элементов последовательности
print(sum(numbers))

# enumerate - нумерация последовательности
winners = ['Leo','Max','Kate']
for number, winner in enumerate(winners, 1):
    print(number, winner)

# Пример
# Пользователь вводит три числа. Найти max. min, sum и вывести на экран

numbers = []
for i in range(3):
    number = int(input(f'Введите число № {i+1}: '))
    numbers.append(number)
print(numbers)
print(f'Max: {max(numbers)}')
print(f'Min: {min(numbers)}')
print(f'Sum: {sum(numbers)}')

# Первая функция
def get_sep(sep, sep_len):
    return sep * sep_len

# используем знак разделителя и меняем длину
print(get_sep('*', 100))
print(get_sep('-', 60))

# встраиваем в текст возврат
sep = get_sep('-', 20)
text = 'Hello {} Func {}'.format(sep, sep)
print(text)  
def helloMax():
    print('Hello', 'Max')

helloMax()

def hello(who):
    print('Hello', who)

hello('Max')
hello('Leo')

def greeting(who, say):
    print(say, who)

greeting('Max', 'Hi')
greeting('Leo', 'Hello')

# Параметры по умолчанию
def greeting(who, say='Hello'):
    print(say, who)

greeting('Max')
greeting('Max', 'Hi')

# args - принято называть 
#  *args - позиционные параметры. в фунцию приходит кортеж (имя просто принято, можно менять, главное *)
# **kwargs - именованные параметры. приходит словарь (имя просто принято, можно менять, главное **)
def greeting(say, *args ): # не who - так принято
    print(say, args)

greeting('Hi', 'Max', 'Leo', 'Kate')

def get_person(**kwargs):
    for k,v in kwargs.items():
        print(k, v)

get_person(name='Leo', age=20, has_car = True)

# Передача функции параметром 
# *Функция тоже объект
def some_f():
    return 10

a = some_f()
print(a)
a = some_f
print(a)
print(a())

def f():
    print('Hello from other f')

def to(f_param):
    # параметром будет функция
    # поэтому внутри мы её вызовем
    f_param()

# Проверяем
to(f)


# возможность не только входных данных, но и входных функций
# внутри функции переменными являются
# алгоритм
# последовательность действий
# сами действия
def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def is_even(number):
    return number % 2 == 0
print (my_filter(numbers, is_even))

# если нужны нечетные числа
def is_odd(number):
    return number % 2 != 0
print (my_filter(numbers, is_odd))

# если нужны числа > 4
def big_4(number):
    return number > 4 

print (my_filter(numbers, big_4))
"""
