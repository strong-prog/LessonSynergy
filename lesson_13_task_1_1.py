"""
С помощью цикла создайте матрицу вида 10x10
И ещё одну - такой же размерности. Числа в матрице выше приведены в
качестве примера (одна из генераций).
Итого у вас должно получиться сперва две матрица одинаковой размерности.
И теперь вам нужно сложить эти две матрицы в третью.
Чтобы, заполнить матрицы различными значениями - воспользуйтесь модулем random.
Задание считается выполненным, если вы напишите алгоритм, который будет
уметь как складывать матрицы, так и генерировать матрица различных
размерностей.
"""

from random import randint


def create_matrix(n1, n2):
    # создание матрицы.
    return [[randint(-100, 100) for _ in range(n1)] for _ in range(n2)]


def sum_matrix(m1, m2):
    # сложение матриц.
    # summ = [[(x + y) for x, y in zip(row1, row2)] for row1, row2 in zip(m1, m2)]

    summ = []
    for row1, row2 in zip(m1, m2):
        sum_row = []
        for n1, n2 in zip(row1, row2):
            sum_row.append(n1 + n2)
        summ.append(sum_row)

    return summ


print('Определите размерность матрицы:')
x, y = int(input('x -> ')), int(input('y -> '))

matrix1 = create_matrix(x, y)
print('Матрица 1:', matrix1, sep='\n')

matrix2 = create_matrix(x, y)
print('Матрица 2:', matrix2, sep='\n')

# сложение матриц.
matrix3 = sum_matrix(matrix1, matrix2)
print('Сложение матриц:', matrix3, sep='\n')
