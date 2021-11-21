'''
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
'''

wearhouse_list = []

class Warehouse:
    def __init__(self, number, name, price, quantity):
        self.number = number
        self.name = name
        self.price = price
        self.quantity = quantity

    def add(self):
        while True:
            list = {'Номер': self.number, 'Название модели': self.name, 'Цена за единицу': self.price, 'Количество': self.quantity}
            wearhouse_list.append(list)
            a = '|'
            print('\n---------------------------------- Всего на складе ----------------------------------')
            for i in wearhouse_list:
                i = str(i)
                print(a + i + a)
                print('-------------------------------------------------------------------------------------')
            break

class Printer(Warehouse):
    def func(self):
        return print('Печатает...')


class Scanner(Warehouse):
    def func(self):
        return print('Сканирует...')


class Copier(Warehouse):
    def func(self):
        return print('Копирует...')


unit_1 = Printer('Apple', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
unit_1.add()
unit_2.add()
unit_3.add()
unit_1.func()
unit_2.func()
unit_3.func()