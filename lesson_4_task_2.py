"""
Дано пятизначное целое число. Напишите алгоритм, который возведёт
количество десятков в степень количества единиц. Затем умножит это число
на количество сотен. И делит получившееся число на разность количества
десятков тысяч и количества тысяч.
"""

a, b, c, d, e = map(int, [n for n in input('Введите пятизначное число:')])
print(f'Ответ: {d ** e * c / (a - b)}')