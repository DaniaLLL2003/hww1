'''Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''

with open('new_file.txt', 'a') as file:
    while True:
        data = input('Напишите что-нибудь: ')
        file.write(data + '\n')
        if not data:
            break