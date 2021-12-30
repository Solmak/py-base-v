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


def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result

# lambda - неименованная,
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print (my_filter(numbers, lambda number: number % 2 == 0))
print (my_filter(numbers, lambda number: number % 2 != 0))
print (my_filter(numbers, lambda number: number > 4))
"""

# sorted  - сортировка последовательности
# sorted(iterable, *, key=None, reverse=False)
# аргументы: последовательность, ключ для сортировки, порядок

# набот чисел
numbers = [1,7,4,6,3,9,1,2]
# по возр
print(sorted(numbers))
# по убыв
print(sorted(numbers,reverse=True))

# набор строк
names = ['Max', 'Leo', 'Kate', 'John']
# по алфав
print(sorted(names))

# города и числ насел (условные)
cities = [('Москва', 1000), ('Paris', 2000), ('Vegas', 500)]
# по умолч сраб по алфав
print(sorted(cities))
# как по населению?
def by_count(city):
    return city[1]

print(sorted(cities, key=by_count))
# или лямбда
print(sorted(cities, key=lambda city: city[1]))

# filter - фильтрация последовательностей
# filter(function, iterable)
# аргументы: функция фильтрации, последовательность

# набор чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# получить только четные
result = filter(lambda number: number % 2 == 0, numbers)
print(result)
print(type(result))
result = list(result)
print(result)

# набор строк
names = ['Max', 'Leo', 'Kate']

# получить строки больше 3-х символов
print(list(filter(lambda name: len(name) > 3,names))) 

# map - применение функции к каждому элементу последовательности
# map(func, iterable, ...)
# аргументы: функция, последовательность

# набор чисел
numbers = [2, 3, 5, 8]
# получить список квадратов чисел
print(list(map(lambda x: x**2, numbers)))
# привести числа к строке
print(list(map(lambda x: str(x), numbers)))



