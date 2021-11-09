'''

Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

'''

class Car:
    def __init__(self, name, color, speed, is_police:bool):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        motion = input('Куда ехать? ')
        if motion == 'w':
            return print(f'{self.name} едет прямо ')

    def stop(self):
        stop_motion = input('Остановиться? ')
        if stop_motion == 's':
            return print(f'{self.color} {self.name} остановился ')

    def turn(self):
        turn_motion = input('Куда поворачивать? ')
        if turn_motion == 'd':
            return print(f'{self.color} {self.name} повернул направо ')
        if turn_motion == 'a':
            return print(f'{self.color} {self.name} повернул налево ')

    def show_speed(self):
        return print(f'Скорость {self.name} составляет {self.speed} км/час ')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f'Скорость превышает 60 км/час. Будьте осторожны! ')
        else:
            return print(f'Скорость {self.name} составляет {self.speed} км/час ')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f'Скорость превышает 40 км/час. Будьте Осторожны! ')
        else:
            return print(f'Скорость {self.name} составляет {self.speed} ')

class SportCar(Car):
    pass

class PoliceCar(Car):
    def lights(self):
        if self.is_police == True:
            return print('Мигалки включены ')
        else:
            return print('Это не полицейская машина! ')


ferrari = Car('Феррари', 'красный', 300, False)
camry = TownCar('Камри', 'синяя', 100, False)
lada = WorkCar('Лада', 'Жёлтая', 50, False)
kia = PoliceCar('Киа', 'Белая', 100, True)

kia.go()
kia.show_speed()
kia.lights()
kia.turn()
kia.stop()