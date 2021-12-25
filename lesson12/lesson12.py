# -----------------------------------------------------
# Функция open
# открывает файл в указанном режиме
# f = open(‘my.txt’, ‘w’)
# file — имя файла
# mode — режим
# encoding — кодировка

# Режимы открытия mode
# r — чтение
# w — запись, если файла нет, создается новый
# x — запись, если файла нет, ошибка
# a — дозапись
# b — двоичный режим
# + — открытие на чтение и запись

# открываем на запись 
# - файла не существует - будет создан новый 
# ! - если файл существует - ОН БУДЕТ ПЕРЕЗАПИСАН
# f = open('lesson12\\first.txt', 'w')

# открываем на чтение - файла не существует - выдаст ошибку
# f = open('second.txt', 'r')

# открываем на чтение - файл существует
# f = open('lesson12\\first.txt', 'r')

# -----------------------------------------------------
# Запись текста в файл
# write — записать строку в файл, строки не переносятся
# writelines — записать список строк в файл, строки не переносятся
# \n — символ конца строки

# f = open('lesson12\\first.txt', 'w')
# f.write('Hello!\n')
# f.write('World\n')
# f.writelines(['Hello\n','Python\n'])

# -----------------------------------------------------
# Чтение из файла
# read — чтение всего файла
# for line in f: — чтение файла построчно
# readlines — чтение файла в список строк

# f = open('lesson12\\first.txt', 'r')
# print(f.read())   # если не закомментить - не прочитает. Указатель позиции?
# for line in f:
#     print(line.replace('\n', ''))
# print(f.readlines())

# -----------------------------------------------------
# Закрытие файла
# После работы с файлом его необходимо закрывать.
# Открытые файлы тратят ресурсы системы.
# f.close().
# Если до close произойдет исключительная ситуация, файл не будет закрыт.
# Удобным вместо close() является использование with.

# f = open('lesson12\\first.txt', 'r')
# for line in f:
#     print(line.replace('\n', ''))
# f.close()    # надо не забывать закрывать - можно избежать с конструкцией whith

# with open('lesson12\\first.txt', 'r') as f: # закроется автоматически когда закроется whith
#     for line in f:
#         print(line.replace('\n', ''))
# print('end')

# -----------------------------------------------------
# # Типы строк в Python
# # str — обычные строки
# # bytes — строки байт
# # bytearray — изменяемая строка байт

# # создание обычной строки
# s = 'Hello world'
# print(type(s))

# # создание строки байт
# sb = b'Hello bytes'
# print(type(sb))
# print(sb)

# -----------------------------------------------------
# Действия со строками байт. Различия с обычной
# индекс sb[0]
# срез sb[1:3]
# ...

# s = 'Hello world'
# sb = b'Hello bytes'

# print(s[1])
# print(sb[1])
# print(s[1:3])
# print(sb[1:3])

# for item in sb:
#     print(item)

# -----------------------------------------------------
# Как строка хранится в памяти?
# Любая информация хранится в памяти как набор 0 и 1.
# Строки не являются исключением.
# Каждому символу ставится в соответствие определенный код (число).
# Коды могут быть разные и зависят от кодировки.
# sb = b'Ad'

# # по acsii должно получиться 65
# print(sb[0])
# # по acsii должно получиться 100
# print(sb[1])

# -----------------------------------------------------
# Перевод строки в байты (кодирование)
# ‘Hello world’.encode(‘utf-8’).
# При переводе строки str в байты bytes указываем кодировку.
# Кодировка должна поддерживать символы нужного нам алфавита.

# s = 'Hello world Мир'
# sb = s.encode('utf-8')
# print(type(sb))
# print(sb)

# # Перевод байт в строку (декодирование)
# # sb.decode(‘utf-8’).
# # Указываем кодировку, которой мы кодировали строку.
# s1 = sb.decode('utf-8')
# print(type(s1))
# print(s1)

# -----------------------------------------------------
# Работа с файлом в режиме байтов
# open(‘filename’, ‘wb’) — режим записи байтов
# open(‘filename’, ‘rb’) — режим чтения байтов
# параметр encoding определяет кодировку
# open(‘filename’, ‘w’, encoding=’utf-8’)

# Открываем файл для записи байтов. Кодировка тут не треба, ведь открываем в двоичном виде
with open('lesson12\\bytes.txt', 'wb') as f: # закроется автоматически когда закроется whith
    pass
# Открываем файл для чтения байтов. Кодировка -
with open('lesson12\\bytes.txt', 'rb') as f: 
    pass
# открываем в текстовим виде с указанием кодировки
with open('lesson12\\bytes.txt', 'r', encoding='utf-8') as f: 
    pass

# Запись байтов в файл
# f.write(b’some bytes’) — файл открыт в режиме wb
# f.write(‘some str’) — файл открыт в режиме w
# в любом случае информация хранится в виде нулей и единиц


