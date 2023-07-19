"""
Подробный требуемый функционал:

Функция create:
- Данная функция будет создавать новую запись с информацией о питомце и добавлять эту информацию в наш словарь pets.
Функция read:
- Данная функция будет отображать информацию о запрашиваемом питомце в виде:
  Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша.
Функция update:
- Данная функция будет обновлять информацию об указанном питомце.
Функция delete:
- Данная функция будет удалять запись о существующем питомце.

Словарь pets:
pets = {1:{"Мухтар": {"Вид питомца": "Собака", "Возраст питомца": 9, "Имя владельца": "Павел"},},
        2:{"Каа": {"Вид питомца": "желторотый питон", "Возраст питомца": 19, "Имя владельца": "Саша"},},
        # и так далее
    }

Суть будущей программы будет заключаться в следующем:

- Программа будет работать с помощью цикла while с условием command
!= 'stop', то есть до тех пор, пока на предложение ввести команду,
пользователь не введёт слово stop

- Перед взаимодействием с "базой данных" запрашивается одна из
команд в качестве пользовательского ввода. Пусть это будет
переменная command

- Функция create должна добавлять новую информацию таким образом,
чтобы идентификатор увеличивался на единицу. Чтобы у вас была
возможность получать последний ключ в словаре воспользуйтесь
импортом модуля collections. В начале вашей программы пропишите
строчку: import collection, а в функции create в первых строках пропишите
следующий код:
def create():
last = collections.deque(pets, maxlen=1)[0]
last в данном случае и будет число последнего ключа (или в нашей
логике - идентификатора записи). Именно его и необходимо будет
увеличивать на единицу при добавлении следующей записи.

Чтобы не повторяться в коде, вам нужно создать такие функции:
get_pet(ID):
- функция, с помощью которой вы получите информацию о питомце в виде словаря
- сделайте проверку, если питомца с таким ID нет в нашей "базе данных" верните в этом случае False
  а если питомец всё же есть в "базе данных" - верните информацию о нём

get_suffix(age):
- функция, с помощью которой можно получить суффикс 'год', 'года', 'лет'
  реализацию этой функции вам предстоит придумать самостоятельно
- функция будет возвращать соответствующую строку

pets_list():
- эта функция будет создана для удобства отображения всего списка питомцев

Обратите внимание, если ID не существует в словаре с питомцами - будет
возникать ошибка. Вам можно от неё избавиться, если правильно составить
проверочное условие. Здесь не потребуется использовать такие конструкции,
как try, except, чтобы обработать возникшую ошибку
"""
import collections
from numdeclination import NumDeclination


def get_suffix(age):
    nd = NumDeclination()
    converted = nd.declinate(int(age), ["год", "года", "лет"], type=1)

    return converted.number, converted.word


def read():
    #  Отобразить информацию о запрашиваемом питомце вида:
    #  Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша
    pet_read = get_pet()
    if pet_read:
        data_list = []

        for key in pet_read.keys():
            data_list.append(key)
            for value in pet_read[key].values():
                data_list.append(value)

        print(f'Это {data_list[1]} по кличке "{data_list[0]}". '
              f'Возраст питомца: {get_suffix(data_list[2])[0]} {get_suffix(data_list[2])[1]}. '
              f'Имя владельца: {data_list[3]}.')
    else:
        print('-->  С таким ID питомца нет.')


def delete():
    #  Удалить запись о существующем питомце.
    pet = get_pet()

    if pet:
        global pets
        new_dict = {key: val for key, val in pets.items() if val != pet}
        pets = new_dict
        print('-->  Запись удалена.')
    else:
        print('-->  С таким ID питомца нет.')


def update():
    #  Обновить информацию об указанном питомце.
    pet = get_pet()

    if pet:
        for i in data_keys:
            data_input = input(f'{i.capitalize()}: ')

            if i == 'кличка питомца':
                pet[data_input] = pet.pop(list(pet.keys())[0])
            elif i == 'возраст питомца':
                while True:
                    if data_input.isdigit():
                        pet[list(pet)[0]][i] = data_input
                        break
                    print('-->  Введите возраст числом!')
                    data_input = input(f'{i.capitalize()}: ')
            else:
                pet[list(pet)[0]][i] = data_input
        print('-->  Запись обновлена.')
    else:
        print('-->  С таким ID питомца нет.')


def pets_list():
    # Отобразить весь список питомцев.
    # Информацию по каждому питомцу можно вывести с помощью цикла for.
    if len(pets) > 0:
        for pet_l in pets.items():
            print(pet_l)
    else:
        print('-->  Записей нет.')


def get_pet() -> dict:
    # Получить информацию о питомце в виде словаря.
    # Сделать проверку, если питомца с таким ID нет "базе данных" вернуть False,
    # если питомец есть в "базе данных" - вернуть информацию о нём.
    print('Ведите ID питомца: ')
    id_pet = int(input('-->  '))

    return pets[id_pet] if id_pet in pets.keys() else False


def crete():
    #  Создать новую запись с информацией о питомце и добавить эту информацию в словарь pets.
    try:
        last_id = collections.deque(pets, maxlen=1)[0]
    except IndexError:
        last_id = 0

    last_id += 1
    pets[last_id] = {}

    for i in data_keys:
        data_input = input(f'{i.capitalize()}: ')

        if i == 'кличка питомца':
            pets[last_id][data_input] = {}
        elif i == 'возраст питомца':
            while True:
                if data_input.isdigit():
                    pets[last_id][list(pets[last_id])[0]][i] = int(data_input)
                    break
                print('-->  Введите возраст числом!')
                data_input = input(f'{i.capitalize()}: ')
        else:
            pets[last_id][list(pets[last_id])[0]][i] = data_input
    print(f'-->  Запись создана с ID: {last_id}')


def start():
    while True:
        print('Введите команду: create, pets_list, update, delete, read, stop')
        command = input('-->  ')

        if command == 'stop':
            print('-->  Программа завершена!')
            break
        elif command in command_dict:
            command_dict[command]()
        else:
            print('-->  Такой команды нет!')
        print()


pets = dict()
data_keys = ['кличка питомца', 'вид питомца', 'возраст питомца', 'имя владельца']
command_dict = {
    'create': crete,
    'pets_list': pets_list,
    'update': update,
    'delete': delete,
    'read': read,
}

start()
