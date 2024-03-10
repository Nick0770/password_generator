from random import choice 
from time import sleep
from sys import exit

vari = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n','m'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N','M'],
        ['`', '~', '!', '#', '$', '%', '^', '*', '&', '(', ')', '-', '_', '+', '=', '|', '[', ']', '{', '}', ':', ';', '"', '<', '>''/', '?', ',', '.']] #  это всё - варианты символов в пароле

#  функция для выключения программы в любом месте
def off(res):
    if res == 0:
        exit()

while True:
    sleep(0.3)
    print('Чтобы прекратить работу, нажмите 0 во время любого ввода!')
    sleep(0.3)
    #  цикл для ввода длины пароля, чтобы избежать ошибок от пользователя
    while True:
        try:
            user_choice = int(input('Введите длину пароля (минимальная длина - 4): ')) 
            off(user_choice)
            if user_choice < 4:
                continue
            break
        except ValueError:
            print('Длина пароля должна быть числом!')
            continue

    password = '' # сюда записывается пароль

    #  цикл для создания пароля
    for i in range(user_choice):
        password += choice(choice(vari))

    #  это контроль пароля, чтобы он был максимально усложнённым
    def control(string: str, variant: list): 
        for i in variant:
            if i in string:
                print('Проверка пройдена!')
                sleep(0.2)
                return ''
        print('Длина пароля изменена для большей безопасности!')
        sleep(0.2)
        return choice(variant)

    password += control(password, vari[0]) + control(password, vari[1]) + control(password, vari[2]) + control(password, vari[3])

    print(f'Ваш пароль: {password}')

    #  сохранение в txt
    while True:
        try:
            save = int(input('Хотите ли вы сохранить пароль в .txt файл? (1 - да, 2 - нет): '))
            off(save)
            if save != 1 and save != 2 and save != 0:
                continue
            break
        except ValueError:
            print('Выбор должен быть числом!')
            continue

    if save == 1:
        direction = input('Для чего этот пароль?: ')
        if direction == '0':
            exit()

        while True:
            try:
                path = input('Введите полный путь к файлу!:')
                if path == '0':
                    exit()
                if type(path) != str:
                    continue
                if path[-4::] != '.txt':
                    print('Генератор сохраняет только в .txt файлы')
                    continue
                break
            except ValueError:
                print('Путь должен быть строкой!')
                continue

        
        with open(path, 'a', encoding='utf-8') as file:
            file.write(f'{direction}: {password} \n')
            print('Пароль успешно сохранён!')
    

