# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). 
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код. 
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
# lesson10_pt_dir.py

# 2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. 
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
#     Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
# lesson10_pt_rnd.py

# 3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций. 
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.
import os
import lesson10_pt_dir as dir
import lesson10_pt_rnd as rnd

print(os.listdir())
dir.makedirs()
print(os.listdir())
dir.rmdirs()
print(os.listdir())

my_list = [1, 2, 3, 4, 5, 67, 12]
print(rnd.rnd_list(my_list))