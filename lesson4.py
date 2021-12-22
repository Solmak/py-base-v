# кавычки внутри 
print('say "Hello"')
print("say 'Hello'")

# доступ к элементу строки по индексу
string = 'Hello'
print(string[0])
print(string[1])
print(string[3])
print(string[4])

# можно использовать отрицательные индексы string[-2, отсчет ведется с конца -1 - это последний
print(string[-1])
print(string[-2])
print(string[-3])
print(string[-4])
print(string[-5])

# срезы через : первое индекс, второое сколько берем
print(string[1:3])
print(string[2:4])
print(string[:3]) # с первого
print(string[2:]) # до последнего

# Функция len(), и методы find, split, isdigit, upper, lower
string = 'Просто лошадь'
print(len(string))
print(string.find('ло')) #индекс первого элемента строки поиска
print(string.find('лоdsaf')) # -1 если не нашел

print(string.split()) # без параметров разбивает по пробелам
print(string.split(';')) # параметр - разделитель
string = 'Просто;лошадь'
print(string.split(';'))

print(string.isdigit())    # проверятет, состоит ли только из цифр. Возвращает boolean
string = '294832904892348902038'
print(string.isdigit())

string = 'Просто лошадь'
print(string.upper())   # переводит в верхний регистр
print(string.lower())   # в нижний

# форматирование строк
name = 'Leo'
age = 30
# 1. конкатенация - не рекомендуется
hello_str = 'Привет ' + name + ', тебе ' + str(age) +' лет'
print(hello_str)
# 2. % 
hello_str = 'Привет %s, тебе %d лет'%(name, age)
print(hello_str)
# 3. format - рекомендуется
hello_str = 'Привет {}, тебе {} лет'.format(name, age)
print(hello_str)

top5 = 'Первые 5 мест на соревнованиях: 1. Иванов 2. Петров 3. Пупкин 4. Сидоров 5. Деревянко'
# Надо вывести "Поздравляем 1. ИВАНОВ 2. ПЕТРОВ 3. ПУПКИН с успехом"
start  = top5.find('1.')    # ищем начало нужного
end = top5.find('4.') - 1      # конец
top3 = top5[start:end]
result = 'Поздравляем {} с успехом'.format(top3.upper())
print(result)

# списки list
some_list = []  # empty list
friends = ['Max','Leo', 'Kate']
print(friends)
print(type(friends))
# индексы как в строках, работают срезы. срезы возвращают list
print(friends[1])
print(friends[-1])
print(friends[:2])
# len, append, pop, clear
print(len(friends)) # длина
friends.append('Ron') # добавляет в конец
print(len(friends))
print(friends.pop()) # удаляет последний и возвращает его
print(len(friends))
friends.clear() # очистка списка
print(friends)
friends = ['Max','Leo', 'Kate','Leo']
friends.remove('Leo') # удаляем по значению только первое
print(friends)
del friends[1] # удаляем по индексу
print(friends)

# in - проверяет наличие элемента в списке и возвращает boolean. Так же работает и со строками - проверяет подстроку
print('Max' in friends)

hero = 'Superman'
if hero.find('man') != -1:
    print('Есть')

if 'man' in hero:
    print('Есть')

goals = ['стать гуру в Python', 'выпить таблетки', 'покормить верблюда']
if 'выпить таблетки' in goals:
    print('не забыли')


'''
Соревнования по Python
Пользователь вводит количество участников и их места в зависимости от количества
1. Вывод имен участников по алфавиту
2. Получить 3-х победителей и поздравить их
3. Победители: ... Поздравляем!
'''

print('СОРЕВНОВАНИЯ ПО PYTHON')
count = int(input('Введите количество участников: '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место: '.format(i))
    members.append(name)
    i -= 1



# вывод участников по алфавиту
# sorted - функция
print('В соревнованиях участвовали: ', sorted(members))

# * мы записади людей с конца reverse
members.reverse()



# Нужно взять первые три места
result = members[:3]
result = 'Победители: {} Поздравляем!'.format(result)
print(result) 

# for in
friends = ['Max','Leo', 'Kate']
# так с while
i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1
# а так с for
for friend in friends:
    print(friend)

string = 'Просто строка'
for letter in string:
    print(letter)

roles = ('admin','guest','user')    # touple
for role in roles:
    print(role)

# range - создает последовательность целых чисел range(start_stop, stop, [step])
numbers = range(10)
print(numbers)
print(type(numbers))
print(list(numbers))

winners = ['Max', 'Leo','Kate']
for winner in winners:
    print (winner)

# каке вывести с местом
for i in range(len(winners)):
    print (i+1, ') ', winners[i])
# или
for i in range(1,len(winners)+1):
    print (i, ') ', winners[i-1])

# словарь - неупорядоченная коллекция с доступом по ключу my_dict = {key1: value1, key2: value2, ...}
friend = {
    'name': 'Max',
    'age': 23
}
print(friend['age'])
# добавление или изменение в словаре
friend['has_car'] = True # добавилось значение, если бы уже было, то далось бы соответственное значение
print(friend)

del friend['age'] # удаление пары ключ-значение
print(friend)

if 'age' in friend: # in работает по ключу
    print('Есть возраст')
if 'has_car' in friend:
    print('Есть машина')

# перебор в for может работать по ключам, значениям и парам ключ-значение
friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}

# по ключам
for key in friend.keys():
# или for key in friend:  - тоже перебирает по ключам
    print(key)
    print(friend[key])

# по значениям
for val in friend.values():
    print(val)

# по парам ключ-значение
for item in friend.items(): # вернет кортежи
    print(item)

for key, val in friend.items(): # Разбиваем кортежи на 2 переменные
    print(key, val)


# множества - коллекции с неповторяющимися элементами, одинаковых значений быть не может
# set = {'Berlin','Paris','Moscow'}
cities = ['Berlin','Paris','Moscow','Las Vegas', 'Moscow']
print (cities)
print (set(cities))

# Действия со множествами
cities = {'Berlin','Paris','Moscow','Las Vegas', 'Moscow'}
print (cities)
# add - добавление
cities.add('Burma')
print (cities)
# remove - удаление элемента
cities.remove('Moscow')
print (cities)
# len()
print (len(cities))
# in - работает
print ('Paris' in cities)

for city in cities:
    print(city)


# операции со множествами
# Объединение - |
# Пересечение - &
# Разность - -

# ВЕЩИ В ОТПУСК
# Max взял
max_things = {'Телефон','Бритва','Рубашка','Шорты'}
# Kate взяла
kate_things = {'Телефон','Шорты','Зонтик','Помада'}

# какие вещи взяли вместе
print(max_things | kate_things) # Обьединение
# какие повторяются
print(max_things & kate_things) # Пересечение
# какие взял max, но не взяла kate 
print(max_things - kate_things) # Разность - вычитание
# какие взяла kate, но не взял Max 
print(kate_things - max_things) # Разность - вычитание
