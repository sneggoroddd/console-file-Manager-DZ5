choice = 0
balance = 0
pokupka = 0
history = []
cont='Yes'
while cont=='Yes':
    print("1. пополнение счета")
    print("2. покупка")
    print("3. история покупок")
    print("4. выход")
    print("5. Баланс")
    choice = input('Выбери пункт меню:')
    if choice == '1':
        balance = int(input('введите сумму пополнения баланса:'))
    elif choice == '2':
        pokupka = int(input('введите сумму покупки:'))
        if balance - pokupka < 0:
            print('Недостаточно средств')
        else:
            balance = balance - pokupka
            name = input('введите название покупки:')
            history.append((name,pokupka))
    elif choice == '3':
        print(history)
    elif choice == '4':
        print('Спасибо за пользование сервисом')
        cont = 'No'
    elif choice == '5':
        print("Ваш баланс:", balance)
    else:
        print("неверный пункт меню")