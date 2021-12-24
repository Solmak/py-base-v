# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). 
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код. 
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
# lesson10_pt_dir.py

import os

def makedirs():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), f'dir_{i}')
        os.mkdir(new_path)

def rmdirs():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), f'dir_{i}')
        os.rmdir(new_path)


if __name__ == '__main__':
    print(os.listdir())
    makedirs()
    print(os.listdir())
    rmdirs()
