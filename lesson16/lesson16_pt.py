"""
Задача
Консольный файловый менеджер.
Создание, удаление, копирование файлов и папок.
Сохранение информации о своей работе в файл.
Игру мы уже писали, тут модуль и команда закомментированы, чтобы еще один модуль не постить
"""
# Домашняя версия. Посмотрел я  на этот ужасный if c try и решил это переписать
import os, shutil
from datetime import datetime

# import game
# Настройки окружения
shell = {
    "name": "My shell",
    "active": True,
    "path": os.getcwd(),
    "log": f"{os.getcwd()}\log.txt",  # чтобы лог не размазывать по директориям при их смене
}

# Запись о работе в файл
def save_info(message):
    current_time = datetime.now()
    result = f"{current_time} - {message}"
    with open(shell["log"], "a", encoding="utf-8") as f:
        f.write(result + "\n")


# Пример лога
# 2021-12-30 12:58:05.755096 - Start session
# 2021-12-30 12:58:18.009992 - create - 1.txt
# 2021-12-30 12:58:24.538807 - dcreate - 111
# 2021-12-30 12:58:39.656858 - exit
# 2021-12-30 12:58:39.657857 - End session
# 2021-12-30 12:59:04.335302 - Start session
# 2021-12-30 12:59:20.188056 - cp 1.txt->2.txt
# 2021-12-30 12:59:29.667046 - cp 111->222
# 2021-12-30 12:59:31.985968 - ls
# 2021-12-30 12:59:37.089379 - cp - неверные аргументы
# 2021-12-30 12:59:41.402639 - cp, [Errno 2] No such file or directory: 'dkslj'
# 2021-12-30 12:59:46.513393 - cp - неверные аргументы
# 2021-12-30 13:00:02.825410 - cp, [Errno 2] No such file or directory: 'dkslj'
# 2021-12-30 13:00:14.970423 - cp 2.txt->1.txt
# 2021-12-30 13:00:18.690612 - cp 2.txt->1.txt
# 2021-12-30 13:00:35.506440 - cp 2.txt->1.txt
# 2021-12-30 13:00:49.234624 - cp, [WinError 183] Невозможно создать файл, так как он уже существует: '111'
# 2021-12-30 13:00:56.458458 - cp 222->333
# 2021-12-30 13:00:58.442450 - cp, [WinError 183] Невозможно создать файл, так как он уже существует: '333'
# 2021-12-30 13:01:01.337187 - exit
# 2021-12-30 13:01:01.338199 - End session


# Функция выхода из оболочки
def shell_exit(args):
    if len(args) > 0:
        print('Команда "exit" не требует аргументов')
    shell["active"] = False
    return "exit"


# функция помощи
def help(args):
    if len(args) > 0:
        print('Команда "help" не требует аргументов')
    print("Возможные команды:")
    print("<param> - обязательный параметр")
    print("/param/ - необязательный параметр")
    print("    exit - выход из оболочки")
    print("    help - вывод этой помощи")
    print("    ls /d/ - список файлов и папок")
    print("        d - показать только папки")
    print("    create <file_name> /text/- создание файла и запись в него /text/")
    print("    dcreate <folder_name>- создание папки")
    print("    del <file_or_folder name>- удаление файла или папки")
    print(
        "    cp <file_or_folder name> <new_file_or_folder name> - копирование файла или папки"
    )
    print("    cd <folder_name>- смена рабочей директории")
    print("    game - компьютер угадывает число")
    return "help"


# Просмотр списка файлов и папок.
def get_list(args):
    if len(args) == 0:
        result = os.listdir()
        print(result)
        return "ls"
    elif len(args) == 1 and args[0] == "d":
        result = os.listdir()
        result = [f for f in result if os.path.isdir(f)]
        print(result)
        return "ls d"
    else:
        result = "ls - неверные аргументы"
        print(result)
        return result


# функция создания файла
def create_file(args):
    if len(args) > 2 or len(args) < 1:
        result = "create - неверные аргументы"
        print(result)
        return result
    text = "".join(args[1:])
    with open(args[0], "w", encoding="utf-8") as f:
        if text:
            f.write(text)
    return f"create - {args[0]}"


# функция создания папки
def create_folder(args):
    if len(args) != 1:
        result = "dcreate - неверные аргументы"
        print(result)
        return result
    os.mkdir(args[0])
    return f"dcreate - {args[0]}"


# удаление папки или файла
def delete_file(args):
    if len(args) != 1:
        result = "del - неверные аргументы"
        print(result)
        return result
    if os.path.isdir(args[0]):
        os.rmdir(args[0])
    else:
        os.remove(args[0])
    return f"del {args[0]}"


# Копирование файлов и папок
def copy_file(args):
    if len(args) != 2:
        result = "cp - неверные аргументы"
        print(result)
        return result
    if os.path.isdir(args[0]):
        shutil.copytree(args[0], args[1])
    else:
        shutil.copy(args[0], args[1])
    return f"cp {args[0]}->{args[1]}"


# смена рабочей директории
def chahge_directory(args):
    if len(args) != 1:
        result = "cd - неверные аргументы"
        print(result)
        return result
    if os.path.isdir(args[0]):
        os.chdir(args[0])
        shell["path"] = os.getcwd()
        return f'cd -> {shell["path"]}'
    else:
        print("Неверный путь")
        return "cd - неверный путь"


# Основное тело. Бесконечный ввод (до exit), с ловлей исключений
commands = {
    "exit": shell_exit,
    "create": create_file,
    "ls": get_list,
    "help": help,
    "dcreate": create_folder,
    "del": delete_file,
    "cp": copy_file,
    "cd": chahge_directory,
    # "game": game
}

save_info("Start session")
while shell["active"]:

    user_input = input(f'{shell["name"]} {shell["path"]} # ')
    user_input = user_input.split(" ")
    # нет комманды и пуста, чтобы просто на Enter не реагировать, как на ошибку
    if not user_input[0]:
        continue
    elif user_input[0] not in commands.keys():
        print(f'Неизвестная команда! Ведите "help" для получения помощи')
        continue

    try:
        # Для тех кто не понимает следующую строку
        # Мы формируем команду пайтону "на лету"
        # Например, при команде "exit", мы берем значение из commands по ключу "exit", это функция shell_exit
        # и добавляем круглые кавычки с остальными аргументами, в нашем случае, пустой список,
        # Получаем shell_exit([]), те вызов функции с параметрами в виде пустого списка.
        # А что?! Так можно было?!!! Да.
        save_info(commands[user_input[0]](user_input[1:]))
    except Exception as e:
        print("Ошибка: ", e)
        save_info(f"{user_input[0]}, {e}")
save_info("End session")
