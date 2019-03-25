import os
import os.path


def showCatalog():
    a = os.listdir(os.getcwd())
    a = str(a)
    a = a.replace("[", "")
    a = a.replace("]", "")
    a = a.replace(" ", "")
    a = a.replace("'", "")
    a = a.replace(",", ", ")
    print('В вашем директории находятся:', a)


def moveUp():
    a = (os.path.split(os.getcwd()))[0]
    os.chdir(a)


def moveDown():
    a = input('Введите название папки: ')
    if os.path.isfile(os.path.join(os.getcwd(), a)):
        a = input('Вы ввели название файла, а не папки. Пожалуйста, повтрите попытку: ')
    while a not in os.listdir(os.getcwd()):
        a = input('Данной папки в текущей директории не обнаруженно. Пожалуйста, повторите попытку: ')
    b = os.path.join(os.getcwd(), a)
    os.chdir(b)


def countBytes(path):
    counter = 0
    _list_ = os.listdir(path)
    try:
        for i in _list_:
            if os.path.isfile(os.path.join(path, i)):
                counter += os.path.getsize(os.path.join(path, i))
            elif os.path.isdir(os.path.join(path, i)):
                counter += os.path.getsize(os.path.join(path, i))
                counter += countBytes(os.path.join(path, i))
    except PermissionError:
        pass
    return counter


def countFiles(path):
    counter = 0
    _list_ = os.listdir(path)
    try:
        for i in _list_:
            if os.path.isfile(os.path.join(path, i)):
                counter += 1
            elif os.path.isdir(os.path.join(path, i)):
                counter += 1
                counter += countFiles(os.path.join(path, i))
    except PermissionError:
        pass
    return counter


def findFiles(target, path):
    new_list = []
    _list_ = os.listdir(path)
    try:
        for i in _list_:
            if target in i and os.path.isdir(os.path.join(path, i)):
                new_list.append(os.path.join(path, i))
                new_list.append(findFiles(target, os.path.join(path, i)))
            elif target not in i and os.path.isdir(os.path.join(path, i)):
                new_list.append(findFiles(target, os.path.join(path, i)))
            elif target in i and os.path.isfile(os.path.join(path, i)):
                new_list.append(os.path.join(path, i))
    except PermissionError:
        pass
    return new_list


def acceptCommand():
    command = int(input('Введите номер команды, которую хотите выполнить: '))
    while command >= 8 and command <= 0:
        command = input('Номер команды введен некорректно, повторите попытку, пожалуйста: ')
    return command


def runCommand(command):
    if command == 1:
        showCatalog()
    elif command == 2:
        moveUp()
    elif command == 3:
        moveDown()
    elif command == 4:
        path = os.getcwd()
        print('В данной директории находится', countFiles(path), 'файлов и каталогов')
    elif command == 5:
        path = os.getcwd()
        print('Размер текущего каталога', countBytes(path), 'байтов')
    elif command == 6:
        path = os.getcwd()
        target = input('Введите имя файла, который хотите найти: ')
        a = findFiles(target, path)
        if len(a) == 0:
            print('Данный файл найден не был.')
        else:
            a = findFiles(target, path)
            a = str(a)
            a = a.replace("[", "")
            a = a.replace("]", "")
            a = a.replace(" ", "")
            a = a.replace(",", "")
            a = a.replace("'", " ' ")
            print(a)
    else:
        return
    return


def main():
    command = 0
    menu = '1. Просмотр каталога \n' \
           '2. На уровень вверх \n' \
           '3. На уровень вниз \n' \
           '4. Количество файлов и каталогов \n' \
           '5. Размер текущего каталога (в байтах) \n' \
           '6. Поиск файла \n' \
           '7. Выход из программы'
    while command != 7:
        print(os.getcwd())
        print(menu)
        command = acceptCommand()
        if command == 7:
            print('Работа программы завершена.')
            break
        else:
            runCommand(command)


if __name__ == "__main__":
    main()
