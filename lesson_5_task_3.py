"""
Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали,
что минимальная сумма инвестиций - X долларов, больше инвестировать
можно сколько угодно. У Майкла A долларов, у Ивана B долларов. Если оба
могут вложиться - выведите 2, если только Майкл - Mike, если только Иван -
Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.
"""

min_invest = int(input('Минимальная сумма инвестиций: '))
cash_mike = int(input('Наличные Майка: '))
cash_ivan = int(input('Наличные Ивана: '))

if cash_mike >= min_invest and cash_ivan >= min_invest:
    print('2')
elif cash_mike >= min_invest or cash_ivan >= min_invest:
    print('1')
else:
    print('0')
