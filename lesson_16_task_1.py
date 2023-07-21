"""
Создайте класс Касса, который хранит текущее количество денег в кассе, у
него есть методы:
- top_up(X) - пополнить на X
- count_1000() - выводит сколько целых тысяч осталось в кассе
- take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не
достаточно денег
"""


class CashBox(object):
    def __init__(self):
        self.cash = 0

    def top_up(self, cash_up):
        self.cash += cash_up

    def take_away(self, cash_back):
        if self.cash - cash_back < 0:
            print('Ошибка! Недостаточно денег в кассе.')
        else:
            self.cash -= cash_back

    def count_1000(self):
        print(f'1000-x купюр в кассе: {self.cash // 1000}')


box = CashBox()
box.top_up(100)
print(f'Денег в кассе: {box.cash}')
box.top_up(1000)
print(f'Денег в кассе: {box.cash}')
box.count_1000()
box.take_away(1000)
print(f'Денег в кассе: {box.cash}')
box.take_away(1000)
print(f'Денег в кассе: {box.cash}')
