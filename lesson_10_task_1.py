"""
У вас должен получиться словарь, с ещё одним словарём внутри. То есть, есть
словарь pets. Он в себе хранит ещё один словарь, который обозначается
именем питомца.
Например:
pets = {
"Мухтар": {
"Вид питомца": "Собака",
"Возраст питомца": 9,
"Имя владельца": "Павел"
}
}
Так должен будет выглядеть результируюший словарь, но первоначальный
его вид - пустой. Его необходимо заполнить пользовательским вводом через
консоль с помощью функции input().
Возраст питомца должен быть типа int Всё остальное - строки
Так как возраст питомца указывается типом int. Необходимо, в соответствии с
указанным возрастом выводит год, года или лет. Например:
Его возраст: 24 года
Его возраст: 21 год
Его возраст: 19 лет
Для получения информации необходимо
воспользоваться методами словаря keys() и values():
Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша.
"""


# в соответствии с указанным возрастом выводим год, года или лет
def years(num):

    last_num = [n for n in str(num)][-1]
    if int(last_num) in (0, 5, 6, 7, 8, 9):
        return 'лет'
    elif int(last_num) in (2, 3, 4):
        return 'года'
    else:
        return 'год'


pets = {}
data_name = ('кличка питомца', 'вид питомца', 'возраст питомца', 'имя владельца')

# создаем словарь, с ещё одним словарём внутри
for i in data_name:
    data_input = input(f'Введите {i}: ')
    if i == 'кличка питомца':
        pets[data_input] = {}
    elif i == 'возраст питомца':
        pets[list(pets.keys())[0]][i] = int(data_input)
    else:
        pets[list(pets.keys())[0]][i] = data_input

data_list = []

# получаем информацию методами словаря keys() и values()
for key in pets.keys():
    data_list.append(key)
    for value in pets[key].values():
        data_list.append(value)

print(f'Это {data_list[1]} по кличке "{data_list[0]}". Возраст питомца: {data_list[2]} {years(data_list[2])}. '
      f'Имя владельца: {data_list[3]}.')
