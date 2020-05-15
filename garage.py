class Garage:
    '''Здесь стоит авто'''

    def Action(self, car):
        while True:
            answ = int(input('Ваши действия?'
                             f'\nВаш баланс- {car.money} монет'
                             '\n 1 - Проверить состояние авто'
                             '\n 2 - Купить улучшения для авто'
                             '\n 3 - Выйти из гаража\n> '))
            if answ == 1:
                print(f'Состояние вашего двигателя {car.hp_engine}'
                      f'\n Состояние колёс {car.hp_wheels}'
                      f'\n Уровень двигателя {car.engine}'
                      f'\n Уровень колёс {car.wheels}')
                continue
            if answ == 2:
                answ = int(input('Вы можете:'
                                 '\n1 - Улучшить двигатель'
                                 '\n2 - Улучшить колёса \n> '))
                if answ == 1:
                    if car.engine <= 3:
                        answ = str(input('Стоимость улучшения 25 монет, берёте? Да\нет\n> ')).lower()
                        if car.money == 0:
                            print('У вас недостаточно денег!')
                        if answ == 'да':
                            if car.money >= 25:
                                car.money -= 25
                                car.engine += 1
                                print('Установлено!')
                                return
                            else:
                                print('Не хватает денег')
                    if 6 >= car.engine >= 5:
                        answ = str(input('Стоимость улучшения 75 монет, берёте? Да\нет\n> ')).lower()
                        if car.money == 0:
                            print('У вас недостаточно денег!')
                        if answ == 'да':
                            if car.money >= 75:
                                car.money -= 76
                                car.engine += 1
                                print('Установлено!')
                                return
                            else:
                                print('Не хватает денег')
                    if 10 >= car.engine >= 6:
                        answ = str(input('Стоимость улучшения 125 монет, берёте? Да\нет\n> ')).lower()
                        if car.money == 0:
                            print('У вас недостаточно денег!')
                        if answ == 'да':
                            if car.money >= 125:
                                car.money -= 125
                                car.engine += 1
                                print('Установлено!')
                                return
                            else:
                                print('Не хватает денег')
                    if car.engine == 10:
                        print('Извините, больше улучшить не получится!')
                continue
            if answ == 3:
                break
