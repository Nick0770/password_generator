from random import choice 
from time import sleep
from sys import exit

vari = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n','m'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N','M'],
        ['`', '~', '!', '#', '$', '%', '^', '*', '&', '(', ')', '-', '_', '+', '=', '|', '[', ']', '{', '}', ':', ';', '"', '<', '>''/', '?', ',', '.']] #  that's all - variants of characters in the password

#  function to turn off the program anywhere
def off(res):
    if res == 0:
        exit()

while True:
    sleep(0.3)
    print('To stop working, press 0 during any input!')
    sleep(0.3)
    #  loop to enter password length to avoid errors from user
    while True:
        try:
            user_choice = int(input('Enter the password length (minimum length is 4): ')) 
            off(user_choice)
            if user_choice < 4:
                continue
            break
        except ValueError:
            print('Password length must be a number!')
            continue

    password = '' # password is written here

    #  loop to create a password
    for i in range(user_choice):
        password += choice(choice(vari))

    #  this is password control to make it as complex as possible
    def control(string: str, variant: list): 
        for i in variant:
            if i in string:
                print('Verification passed!')
                sleep(0.2)
                return ''
        print('Password length has been changed for greater security!')
        sleep(0.2)
        return choice(variant)

    password += control(password, vari[0]) + control(password, vari[1]) + control(password, vari[2]) + control(password, vari[3])

    print(f'Your password: {password}')

    #  saving to txt
    while True:
        try:
            save = int(input('Do you want to save the password in a .txt file? (1 - yes, 2 - no): '))
            off(save)
            if save != 1 and save != 2 and save != 0:
                continue
            break
        except ValueError:
            print('The choice must be a number!')
            continue

    if save == 1:
        direction = input('What is this password for?: ')
        if direction == '0':
            exit()

        while True:
            try:
                path = input('Enter the full path to the file!: ')
                if path == '0':
                    exit()
                if type(path) != str:
                    continue
                if path[-4::] != '.txt':
                    print('The generator saves only to .txt files')
                    continue
                break
            except ValueError:
                print('The path must be a string!')
                continue

        
        with open(path, 'a', encoding='utf-8') as file:
            file.write(f'{direction}: {password} \n')
            print('Password successfully saved!')
    

