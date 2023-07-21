"""
Создайте класс Черепашка, который хранит позиции x и y черепашки,
а также s - количество клеточек, на которое она перемещается за ход.
У этого класса есть методы:
- go_up() - увеличивает y на s
- go_down() - уменьшает y на s
- go_left() - уменьшает x на s
- go_right() - увеличивает y на s
- evolve() - увеличивает s на 1
- degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
- count_moves(x2, y2) - возвращает минимальное количество действий, за
которое черепашка сможет добраться до x2 y2 от текущей позиции
"""


class Turtle(object):
    def __init__(self, x, y, s):
        self.pos_x = x
        self.pos_y = y
        self.move_s = s

    def go_up(self):
        self.pos_y += self.move_s

    def go_down(self):
        self.pos_y -= self.move_s

    def go_left(self):
        self.pos_x -= self.move_s

    def go_right(self):
        self.pos_x += self.move_s

    def evolve(self):
        self.move_s += 1

    def degrade(self):
        if self.move_s - 1 > 1:
            self.move_s -= 1
        else:
            print('Ошибка! Это дно, деградировать уже некуда.')

    def count_moves(self, x2, y2):
        return abs(((self.pos_x + self.pos_y) - (x2 + y2)) // self.move_s)


turtle = Turtle(x=0, y=0, s=1)
turtle.go_up()
turtle.go_left()
turtle.go_left()
print(turtle.count_moves(x2=0, y2=5))
