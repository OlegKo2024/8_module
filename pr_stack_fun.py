print('Задача "План перехват"')
print('Лучший вариант 1')


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


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать

print('Вариант 2')


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for i in numbers:
            try:
                result += i
            except TypeError as exc:
                print(f'Некорректный тип данных для подсчёта суммы - {i}: {exc}')
                incorrect_data += 1
    except TypeError as exc:
        print(f'В numbers записан некорректный тип данных {numbers}: {exc}')
        # return None
    return result, incorrect_data


def calculate_average(numbers):
    sum_numbers = personal_sum(numbers)
    print(sum_numbers)
    try:
        return sum_numbers[0] / (len(numbers) - sum_numbers[1])
    except ZeroDivisionError:
        return 0
    except TypeError as exc:
        print(f'В numbers записан некорректный тип данных - {numbers}: {exc}')


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
