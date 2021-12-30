import os
import shutil
import datetime

# функция создания файла
def create_file(name, text=None):
    with open(name, "w", encoding="utf-8") as f:
        if text:
            f.write(text)


# функция создания папки
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Такая папка уже существует")


# расширим функционал
# Просмотр списка файлов и папок.
def get_list(Folders_only=False):
    result = os.listdir()
    if Folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# удаление папки или файла
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


# Копирование файлов и папок
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print("Такая папка уже существует")
    else:
        shutil.copy(name, new_name)


# Запись о работе в файл
def save_info(message):
    current_time = datetime.datetime.now()
    result = f"{current_time} - {message}"
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(result + "\n")

# смена рабочей директории
def chahge_directory(name):
    if os.path.isdir(name):
        os.chdir(name)
    else:
        print('Неверный путь')

if __name__ == "__main__":
    create_file("test.txt")
    create_file("test.txt", "some text")
    create_folder("new_f1")
    get_list()
    get_list(True)
    delete_file("new_f1")
    delete_file("test.txt")
    copy_file("new_f", "new_f2")
    create_file("test.txt", "123")
    copy_file("test.txt", "test2.txt")
    save_info("Tram-pam-pam")
    get_list()