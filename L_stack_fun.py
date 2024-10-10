print('Сложные моменты и исключения в стеке вызовов функции')

print('Пример 1')
def f01(number):
    return 10 // number

def f02():
    print('Хороший день!')      # 1 строка: Хороший день!
    result_f01 = f01(0)

try:
    total = f02()
    print(total)

except ZeroDivisionError as exc:
    print(f'Класс: {exc}')      # 2 строка: Класс: integer division or modulo by zero

print(f01(2))                   # 3 строка: 5

print('Пример 2')
def f01(number):
    return 10 // number

def f02():
    print('Хороший день!')      # 1 строка: Хороший день!
    summ = 0
    for i in range(-1, 5):
        summ = f01(i)
    return summ

try:
    total = f02()
    print(total)

except ZeroDivisionError as exc:
    print(f'Класс: {exc}')      # 2 строка: Класс: integer division or modulo by zero

print(f01(2))                   # 3 строка: 5

print('Пример 3 - отвлечение на тему списка и append vs extend')
def f01(number):
    return 10 // number

def f02():
    print('Хороший день!')
    summ = 0
    list_summ = []
    for i in range(1, 5):
        summ = f01(i)
        list_summ.append(summ) # Если функция возвращает число, используйте .append(), если список — то .extend()
        # .extend() распакует и добавит каждое число списка в список
    return list_summ

try:
    total = f02()
    print(total)

except ZeroDivisionError as exc:
    print(f'Класс: {exc}')

print(f01(2))                   # 3 строка: 5

print('Пример 4')
def f01(number):
    return 10 // number

def f02():
    print('Хороший день!')
    summ = 0
    for i in range(-2, 3):
        summ += f01(i)
        print(summ)
    return summ

try:
    total = f02()       # ВАЖНО: ТАК КАК ПРОГРАММА НЕ ДОШЛА ДО КОНЦА РЕЗУЛЬТАТ TOTAL НЕ СОХРАНИЛСЯ, РЕЗУЛЬТАТА НЕТ
    print(f'Итак результат: {total}')

except ZeroDivisionError as exc:
    print(f'Класс: {exc}')


# Хороший день!
# -5
# -10
# Класс: integer division or modulo by zero
# 5

print('Пример 5 - перехват исключения на том уровне, где оно возникло')
def f01(number):
    return 10 // number

def f02():
    print('Хороший день!')
    summ = 0
    for i in range(-2, 3, 1):
        try:
            summ += f01(i)
            print(summ)
        except ZeroDivisionError as exc:
            print(f'Внутри f1 что-то пошло не так {exc}, но мы в курсе')
    return summ

try:
    total = f02()
    print(f'Результат: {total}')    # ВАЖНО: ТАК КАК ПРОГРАММА ДОШЛА ДО КОНЦА РЕЗУЛЬТАТ СОХРАНИЛСЯ, TOTAL ЕСТЬ

except ZeroDivisionError as exc:
    print(f'Класс: {exc}')

print('Пример 6 - перехват исключения на том уровне, где оно возникло')
def f01(number):
    return total / number

def f02():
    try:
        result_f1 = f01(i)
        print(result_f1)
    except ZeroDivisionError as exc:
        print(f'Внутри f1 что-то пошло не так {exc}, но мы в курсе')
    return result_f1 / 0

try:
    total = f02()
    print(f'Результат: {total}')    # ВАЖНО: ТАК КАК ПРОГРАММА ДОШЛА ДО КОНЦА РЕЗУЛЬТАТ СОХРАНИЛСЯ, TOTAL ЕСТЬ

except NameError as exc:
    print(f'Класс: {exc}')




