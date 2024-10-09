print('Задание "Программистам всё можно"')

print('Вариант 1')
def add_everything_up(a: (int, float, str), b: (int, float, str)):
    try:
        summa = round(a + b, 3)
        return summa
    except TypeError:
        if isinstance(a, str) or isinstance(b, str):
            return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

print('Вариант 2')
def add_everything_up(a: (int, float, str), b: (int, float, str)):
    try:
        summa = round(a + b, 3)
        return summa
    except TypeError as exc:
        if any([isinstance(a, str), isinstance(b, str)]):
            print(f'Класс: {exc}, Описание: {exc.args}')
            return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
