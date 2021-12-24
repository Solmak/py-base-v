# 2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. 
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
#     Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
# lesson10_pt_rnd.py
import random

def rnd_list(list_name):
    if len(list_name) > 0:
        return random.choice(list_name)
    else:
        return None




if __name__ == '__main__':
    list_name = [1, 2, 3, 4, 5, 67, 12]
    print(rnd_list(list_name))
