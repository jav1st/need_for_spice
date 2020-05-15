from garage import Garage
from car import Car




if __name__ =='__main__':
    car = Car()
    garage = Garage()

    while True:
        place = int(input('Куда идём?'
                          '\n 1 - Гоночная дорога'
                          '\n 2 - Гараж'
                          '\n 3 - На хуй'
                          '\n 4 - Выйти из гонок\n> '))
        if place == 1:
            print('Дороги нет, катитесь на хуй ')
            continue
        if place == 2:
            garage.action(car)
            continue
        if place == 3:
            print('Ну и пиздуй отсюда')
            continue
        if place == 4:
            break