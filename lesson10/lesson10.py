# # импорт модуля целиком
# import math

# # импорт модуля с псевдонимом
# import random as rd

# # ! Сильно не рекомендуется Мы объединяем пространство имен и могут быть накладки
# from math import *
# print(pi)   # После такого импорта, можем не указывать имя модуля

# # Импорт конкретных функций классов или данных. Импортированное тоже помещается в наше пространство имен
# from random import randint, randrange

# print(math.pi)
# print (math.sin(38))
# print(rd.randint(1, 10))
# print(randint(1, 10))

# import math
# # 1. Найти длину окружности с определенным радиусом
# r = 100
# print(f"Длина окружности: {2 * r * math.pi}")

# # 2. Найти площадь окружности с определенным радиусом
# print(f"Площадь окружности: {r**2 * math.pi}")
# print(f"Площадь окружности: {math.pow(r, 2) * math.pi}")

# # 3. По координатам двух точек определить расстояние между ними
# x1 = 10
# y1 = 10
# x2 = 50
# y2 = 100
# l = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# print(f"Расстояние между точками: {l}")
# # 4. Найти факториал числа 9
# print(f"Факториал 9 равен {math.factorial(9)}")

# # Работа с модулем random. Импортируем конкретные функции
# from random import randint, choice, sample, shuffle

# # 1. Загадать случайное число от 0 до 100
# print(randint(0, 100))
# # 2. выбрать победителя из списка players
# players = ["Max", "Leo", "Kate", "Ron", "Bill"]
# print(choice(players))
# # 3. выбрать 3-х победителей из списка players
# print(sample(players, 3))
# # 4. перемешать карты в стопке (списке) cards
# cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
# print(cards)
# shuffle(cards)
# print(cards)

# # Свои модули
# import moda
# from folderb.modb import foo, bar
# # import modc as modc    # выполнится сразу при импорте
# from modc import foo       # опять выполнится. После добавления if __name__ == '__main__' - не выполнится

# print(moda.foo)
# moda.bar()
# print(foo)
# bar()

# # Пакеты - служат для формирования пространства имен. 
# # Работа с модулями с указанием уровня вложенности
# # пакет1.пакет2.модуль
# # import .модуль - внутри пакета из одного модуля в другой
# # import пакет.модуль - стандартно
# # import, from, as ...
# # вложенность пакетов может быть любой (пакет в пакете ...)
# from hospital.h import get_main
# from hospital.patients.index import get_index

# get_main()
# get_index()


# # Модуль os
# # Функции для работы с операционной системой. Не зависит от конкретной ОС
# # name - имя операционной системы
# # chdir - смена текущей директории
# # getcwd() - текущая рабочая директория
# # mkdir() - создание директории (папки)
# # os.path - модуль для работы с путями
# import os

# # Имя операционной системы
# print(os.name)

# # текущая рабочая директория
# print(os.getcwd())

# # создаем новый путь
# new_path = os.path.join(os.getcwd(), 'new_f')

# # coздаем папку по новому пути
# os.mkdir(new_path)

# # Модуль sys
# # Взаимодействие с интерпретатором Python 
# # executable - путь к интерпретатору Python
# # exit() - выход из Python
# # platform - информация об ОС
# # path - список путей поиска модулей
# # argv - список аргументов командной строки
# import sys
# # путь до интерпретатора
# print(sys.executable)
# # Информация о платформе
# print(sys.platform)
# # выход из python
# sys.exit
# print('Этот код мы уже не выполним')

# # sys.path - системный путь. Тип list, т.е. можем ее менять
# import sys
# # import my_module - дает ошибку, не находит модуль

# sys.path.append('C:\Projects')
# for p in sys.path:
#     print(p)

# # В папке с модулем создать 5 подпапок, названия которых состоят из платформы, на которой запущен интерпретатор 
# # и порядкового номера, начиная с 1: win32_1, win_32_2, … Платформа может быть другой.
# import sys, os

# name = sys.platform
# for i in range(1,6):
#     new_path = os.path.join(os.getcwd(), f'{name}_{i}')
#     os.mkdir(new_path)

# Запуск скрипта с парамерами. 
# sys.argv
# список аргументов командной строки при запуске скрипта Python
# sys.argv[0] - путь до скрипта
# остальные параметры передаются при вызове скрипта через пробел
# python my_script.py par1 par2 par3 ...

# import sys

# # print(sys.argv[0])
# for arg in sys.argv:
#     print(arg, type(arg))

# В зависимости от параметра вызывать различные функции скрипта
# Параметр ping -> функция выводит pong
# 2 параметра name <Имя> -> функция приветствия пользователя
# параметр list: показать содержимое текущей директории
import sys, os

def ping():
    print('pong')

def hello(name):
    print(f'Hi! {name}')

def get_info():
    print(os.listdir())

command = sys.argv[1]       # ! при запуске без параметров выдаст ошибку
if command == 'ping':
    ping()
elif command == 'name':
    hello(sys.argv[2])
elif command == 'list':
    get_info()
