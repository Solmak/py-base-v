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
def print_sep():
    print('-' * 100)

print_sep()