print('Задача "План перехват"')

print('Сумма - цикл for с переданными аргументами неименованных параметров')


def personal_sum_(*numbers):
    summa = 0
    for i in numbers:
        summa += i
    return summa


print(personal_sum_(1, 2, 3))

print('Сумма - цикл for и range и переданными аргументами неименованных параметров')


def personal_sum_00(*numbers):
    summa = 0
    for i in range(len(numbers)):
        summa += numbers[i]
    return summa


print(personal_sum_00(1, 2, 3))

print('Сумма - рекурсия со списком')
numbers = [1, 2, 3]


def personal_sum_01(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + personal_sum_01(numbers[1:])


print(personal_sum_01(numbers))

print('Сумма - рекурсия со с переданными аргументами неименованных параметров')


# Ошибка: При использовании summa(*numbers[1:]), важно снова использовать *, чтобы распаковать элементы из среза
# обратно в неименованные аргументы (кортеж). Если просто передать numbers[1:], это будет кортеж из одного элемента
# (т.е. numbers[1:] является отдельным кортежем), и вызовет RecursionError. Функция summa ожидает не именованные
# аргументы, а не один кортеж
# Здесь:
# - numbers[1:] возвращает все элементы, кроме первого, как кортеж.
# - *numbers[1:] распаковывает этот кортеж, так что элементы, содержащиеся в нем, передаются в качестве отдельных
# аргументов в вызове summa.
def personal_sum_03(*numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + personal_sum_03(*numbers[1:])


print(personal_sum_03(1, 2, 3))

print('Сумма - используя функцию sum')


def personal_sum_04(*numbers):
    return sum(numbers)


print(personal_sum_04(1, 2, 3))


print('Сумма - используя функцию sum и списковое выражение, что не нужное усложнение в данном случае')

def personal_sum_05(*numbers):
    return sum(i for i in numbers)


print(personal_sum_05(1, 2, 3)) # но это лишнее самый лучший вариант просто sum(numbers) выше

print('Задача "План перехват"')


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            print(f'В numbers записан некорректный тип данных {i}: {exc}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        sum_numbers = personal_sum(numbers)
        print(sum_numbers)
        print(len(numbers))
    except TypeError as exc:
        print(f'В numbers записан некорректный тип данных {numbers}: {exc}')
        return None
    try:
        return sum_numbers[0] / (len(numbers) - sum_numbers[1])
    except ZeroDivisionError:
        return 0


# print(calculate_average(1, 'str', 3))
# print(calculate_average(42, 15, 36, 13))
# print(calculate_average(str, str, str))

print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать

print('Вариант chatGPT')

print('Вариант 3')


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            print(f'В numbers записан некорректный тип данных {i}: {exc}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple, set)):
        print(f'В numbers записан некорректный тип данных {numbers}')
        return None
    else:
        sum_numbers = personal_sum(numbers)
    try:
        return sum_numbers[0] / (len(numbers) - sum_numbers[1])
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать

