import datetime
import pytz

# Функция для показа всех заметок на экране
def Show_notes():
    file = open("notes.csv", encoding="utf-8")
    show_lines = file.readlines()
    count = 1
    word = ""
    text = ""
    print("\nВсе заметки:\n")
    print("№ \t Заголовок \t Заметка \t Дата сохранения")
    for line in show_lines:
        text += str(count) + " \t "
        for i in line:
            if i != ";":
                word +=i
            else:
                text += word + " \t "
                word = ""
        text += word + " \t "
        print(text)
        count += 1
        text = ""
        word = ""
    file.close()

# Функция для добавления заметки в файл
def Add_note():
    file = open("notes.csv", "a", encoding="utf-8")
    head = input("Введите заголовок заметки: ") + ";"
    note = input("Введите заметку: ") + ";"
    tz = pytz.timezone("Europe/Moscow")
    date_and_time = str(datetime.datetime.now(tz))
    add_word = head + note + date_and_time + "\n"
    file.write(add_word)
    file.close()
    print("\nЗаметка добавлена!\n")

# Функция для редактирования заметки
def Edit_note():
    Show_notes()
    index = int(input("Введите номер строки для редактирования: "))
    
# Открытие файла и его чтение
    file = open("notes.csv", encoding="utf-8")
    lines = file.readlines()
    print("Выбрано: " + lines[index-1] + "\n")

# Инициализация переменных
    word = ""
    head = ""
    note = ""
    date = ""
    count = 0

# Присвоение переменным заголовка заметки и текста заметки
    for i in lines[index-1]:
        if count == 0 and i != ';':            
            word += i
        elif count == 1 and i != ';':            
            word += i        

        elif i == ';' and count == 0:
            head = word 
            word = ""
            count += 1
        elif i == ';' and count == 1:
            note = word 
            word = ""
            count += 1
    
    tz = pytz.timezone("Europe/Moscow")
    while True: # Меню для редактирования
        print("Команды для выбора: ")
        print("1 / head - изменить заголовок")
        print("2 / note - изменить заметку")
        print("3 / exit - выход в главное меню")
        menu = input("Введите команду: ")
        if menu == "1" or menu == "head": # Изменение заголовка заметки
            print("Изменение заголовка заметки!")
            print("\nТекущий заголовок: " + head + "\n")
            word = input("Введите новый заголовок для заметки: ")
            while True:
                agree = input("Сохранить изменения? Y / N: ")
                if agree == "Y" or agree == "y":                
                    date = str(datetime.datetime.now(tz))
                    lines[index-1] = word + ";" + note + ";" + date + "\n"
                    file = open("notes.csv", "w", encoding="utf-8")
                    file.close()
                    file = open("notes.csv", "a", encoding="utf-8")
                    for line in lines:
                        file.write(line)
                    print("Изменения сохранены!")
                    print("Результат: " + lines[index-1])
                    file.close()
                    break
                elif agree == "N" or agree == "n":
                    print("Изменения отменены!")
                    word = ""
                    break
                else:
                    print("\nВозврат в меню выбора команд!\n")   

        elif menu == "2" or menu == "note": # Изменение текста заметки
            print("Изменение заметки!")
            print("\nТекущая заметка: " + note + "\n")
            word = input("Введите новый текст заметки: ")
            while True:
                agree = input("Сохранить изменения? Y / N: ")
                if agree == "Y" or agree == "y":                
                    date = str(datetime.datetime.now(tz))
                    lines[index-1] = head + ";" + word + ";" + date + "\n"
                    file = open("notes.csv", "w", encoding="utf-8")
                    file.close()
                    file = open("notes.csv", "a", encoding="utf-8")
                    for line in lines:
                        file.write(line)
                    print("Изменения сохранены!")
                    print("Результат: " + lines[index-1])
                    file.close()
                    break
                elif agree == "N" or agree == "n":
                    print("Изменения отменены!")
                    word = ""
                    break
                else:
                    print("\nНекорректный ввод!\n")
        elif menu == "3" or menu == "exit":
            print("\nВыход в главное меню!\n")
            break
# Фнукция для удаления заметки из файла
def Remove_note():
    index = int(input("Введите номер пункта для удаления заметки: "))
    file = open("notes.csv", encoding="utf-8")
    lines = file.readlines()
    new_lines = ""
    for line in lines:
        if line != lines[index-1]:
            new_lines += line

    file.close()
    file_write = open("notes.csv", "w", encoding="utf-8") 
    file_write.write(new_lines)
    print("\nОперация выполнена!\n")
    file_write.close()

def Find_note():    
    file = open("notes.csv", "r", encoding="utf-8")
    lines = file.readlines()
    while True:
        count = 1
        task = input("Введите текст для поиска: ")
        if task.lower() in str(lines).lower():
            print("Совпадение найдено: ")
            for line in lines:
                if task.lower() in line.lower():
                    print(str(count) + " - " + line)
                    count +=1
                else:
                    count +=1
        else:
            print("Совпадений не найдено!")
            choice = input("Найти что то еще? Y / Нажмите любую клавишу для отмены: ")
            if choice != "Y" or choice != "y":
                break 

# Основная фукнция с пользовательским меню для управления процессом
def work():    
    while True:
        print("Консольная программа для заметок ")
        print("https://github.com/RussellMorryson ")
        print("#=================================================================================#")
        print("|                                   NOTES                                         |")
        print("#=================================================================================#")
        print("                                Главное меню                                     \n")
        print("                     1 / show    - просмотр всех заметок")
        print("                     2 / add     - добавление заметки")
        print("                     3 / edit    - редактирование заметки")
        print("                     4 / remove  - удаление заметки")
        print("                     5 / find    - поиск заметки")
        print("                     0 / exit    - удаление заметки")
        command = input("\nВведите команду: ")
    
        if command == "1" or command == "show":
            Show_notes()
            input("\nДля перехода в меню нажмите любую клавишу...\n")
      
        elif command == "2" or command == "add":
            Add_note()
            input("\nДля перехода в меню нажмите любую клавишу...\n")
      
        elif command == "3" or command == "edit":
            Edit_note()
            input("\nДля перехода в меню нажмите любую клавишу...\n")
    
        elif command == "4" or command == "remove":
            Show_notes()
            Remove_note()
            input("\nДля перехода в меню нажмите любую клавишу...\n")
        
        elif command == "5" or command == "find":
            Find_note()            
            input("\nДля перехода в меню нажмите любую клавишу...\n")

        elif command == "0" or command == "exit":
            print("\nДо встречи!")
            break
        else:
            print("\nНекорректный ввод!")

# Точка входа
work()