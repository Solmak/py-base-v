"""
Задача
Консольный файловый менеджер.
Создание, удаление, копирование файлов и папок.
Сохранение информации о своей работе в файл.
Текущее видео: создание и проверка основных функций.
"""
import sys
from core import (
    create_file,
    create_folder,
    get_list,
    delete_file,
    copy_file,
    save_info,
    chahge_directory
)

save_info("Start")

try:
    command = sys.argv[1]
except IndexError:
        print("Незадана команда")
        exit()
        
if command == "list":
    try:
        list_param = sys.argv[2]
    except IndexError:
        list_param = False
    else:
        list_param = True if list_param == 'd' else False
    finally:
        get_list(list_param)
elif command == "cr_file":
    try:
        name = sys.argv[2]
    except IndexError:
        print("Неверные параметры команды")
    else:
        create_file(name)
elif command == "cr_fldr":
    try:
        name = sys.argv[2]
    except IndexError:
        print("Неверные параметры команды")
    else:
        create_folder(name)
elif command == "del":
    try:
        name = sys.argv[2]
    except IndexError:
        print("Неверные параметры команды")
    else:
        delete_file(name)
elif command == "cp":   # Не имеет смысла без бесконечного ввода, все равно возвращаемя в исходную после закрытия
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print("Неверные параметры команды")
    else:
        copy_file(name, new_name)
elif command == "cd":
    try:
        name = sys.argv[2]
    except IndexError:
        print("Не задана директория")
    else:
        chahge_directory(name)
elif command == "help":
    print("Возможные команды:")
    print("    list - список файлов и папок")
    print("    list d - показать только папки")
    print("    cr_file - создание файла")
    print("    cr_fldr - создание папки")
    print("    del - удаление файла или папки")
    print("    cp - копирование файла или папки")
    print("    cd - смена рабочей директории")
    print("    help - вывод этой помощи")
else:
    print("неверная команда")

save_info(command)
save_info("end")
