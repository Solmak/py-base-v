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
print(f'Sum: {sum(numbers)}') """

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