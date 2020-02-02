#создаем папку
createFolder = 0
#удаляем папку
remoteFolder = 0
#- копировать (файл/папку) после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;
copyFolder = 0
# просмотр содержимого рабочей директории
# вывод всех объектов в рабочей папке;
viewDirectory = 0
# - посмотреть только папки
# вывод только папок которые находятся в рабочей папке;
viewFolderWork = 0
# - посмотреть только файлы
# вывод только файлов которые находятся в рабочей папке;
viewFileWork = 0
# - просмотр информации об операционной системе
# вывести информацию об операционной системе (можно использовать пример из 1-го урока);
viewOS = 0
# - создатель программы
# вывод информации о создателе программы;
creatorProgram = 0
# - играть в викторину
# запуск игры викторина из предыдущего дз;
playGames = 0
# - мой банковский счет
# запуск программы для работы с банковским счетом из предыдущего дз (задание учебное, после выхода из программы управлением счетом в главной программе сумму и историю покупок можно не запоминать);
accountBank = 0
# - выход
#https://github.com/sneggoroddd/console-file-Manager-DZ5/pull/2
exitProgame = 0
choice = 0
import os
import sys
import shutil
cwd = 0
exit = "no"
while exit == 'no':
    print("1. создать папку")
    print("2. удалить папку")
    print("3. копировать файл/папку")
    print("4. вывод всех объектов в рабочей папке")
    print("5. вывод только папок которые находятся в рабочей папке")
    print("6. вывести информацию об операционной системе")
    print("7. вывод информации о создателе программы")
    print("8. играть в викторину")
    print("10. Выход")
    choice = input('Выбери пункт меню:')
    if choice == '1':
        os.mkdir('new')
    elif choice == '2':
        os.rmdir('new')
    elif choice == '3':
        shutil.copyfile(new, copyNew, follow_symlinks=True)
    elif choice == '4':
        print(os.listdir(path="."))
    elif choice == '5':
        cwd = os.getcwd()
        onlydirs = [d for d in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, d))]
        print(onlydirs)
    elif choice == '6':
        print(sys.platform)
    elif choice == '7':
        print('Savoskin Pavel, Moscow, 2020')
    elif choice == '8':
        import victory
    elif choice == '9':
        import accountBanc
    elif choice == '10':
        exit = "yes"
    else:
        print("неверный пункт меню")