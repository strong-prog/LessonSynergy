"""
Пользователь вводит стороны прямоугольника, выведите его площадь и
периметр. На вход программе могут подаваться как целые числа, так и
вещественные.
"""

print('Введите стороны прямоугольника:')
a, b = float(input('Сторона - a:')), float(input('Сторона - b:'))
square = a * b
perimeter = (a + b) * 2
print(f'Площадь прямоугольника: {square}\nПериметр прямоугольника: {perimeter}')