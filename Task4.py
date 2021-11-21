"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

"""

class Orgtechnic:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def func(self):
        items = {'Модель': self.name, 'Цена': self.price, 'Количество': self.quantity}
        print(items)

class Printer(Orgtechnic):
    def function(self):
        print(f'{self.name} печатает...')

class Scan(Orgtechnic):
    def function(self):
        print(f'{self.name} сканирует...')

class Xerox(Orgtechnic):
    def function(self):
        print(f'{self.name} копирует...')

canon = Printer('Canon', 15000, 5)
canon.function()
canon.func()