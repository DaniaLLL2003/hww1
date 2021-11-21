'''
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return print(f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i')

    def __mul__(self, other):
        return print(f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i')


c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(1, 2)
c1 + c2
c1 * c2