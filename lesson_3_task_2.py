"""
Написать форму ввода ответа на тест по биологии для студентов.
Он должен запрашивать по порядку этапы развития человека.
"""

print('Введите 5 этапов развития человека:')
stage_1, stage_2, stage_3, stage_4, stage_5 = input('1 этап:'), input('2 этап:'), input('3 этап:'), \
    input('4 этап:'), input('5 этап:')
print(f'Этапы: {stage_1} => {stage_2} => {stage_3} => {stage_4} => {stage_5}')
