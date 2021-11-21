'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.

'''

class Division:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide(divider, denominator):
        try:
            return divider / denominator
        except:
            return (f"Делить на нуль нельзя!")

print(Division.divide(10, 0))
print(Division.divide(10, 0.1))
print(Division.divide(8, 4))