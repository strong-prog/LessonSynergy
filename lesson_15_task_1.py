"""
Есть родительский класс:
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
Создайте объект Autobus, который унаследует все переменные и методы
родительского класса Transport и выведете его.
Ожидаемый результат вывода:
Название автомобиля: Renault Logan Скорость: 180 Пробег: 12
"""


class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Autobus(Transport):
    def print_info(self):
        print(f'Название автомобиля: {self.name}. Скорость: {self.max_speed}. Пробег: {self.mileage}.')


bus = Autobus('Renault Logan', 180, 12)
bus.print_info()
