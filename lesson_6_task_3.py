"""
Вводятся целые числа A и B. Гарантируется, что A ≤ B. Выведите все четные
числа на заданном отрезке через пробел.
"""

a, b = int(input('Введите число А: ')), int(input('Введите число B: '))

print(f'Четные числа на отрезке от {a} до {b}:')

for n in range(a, b + 1):
    if n % 2 == 0:
        print(n, end=' ')