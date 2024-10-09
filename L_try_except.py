print('Лекция. Try и Except')

try:
    i = 0
    print(10 / 'a')
    print(10 / i)
    print('завершено')
except:                             # исключение срабатывает вне зависимости от типа ошибки
    print('Нельзя делить на 0')     # Нельзя делить на 0

try:
    i = 0
    # print(10 / 'a')
    print(10 / i)
    print('завершено')
except ZeroDivisionError:           # исключение срабатывает, если это ZeroDivisionError
    print('Нельзя делить на 0')     # Нельзя делить на 0

try:
    i = 0
    pipe = a + b
    print(10 / i)
    print('завершено')
except (ZeroDivisionError, NameError):           # исключение срабатывает, если это ZeroDivisionError или NameError
    print('Нельзя делить на 0 - не выбирает по типу, но и не показывает ошибку')     # Нельзя делить на 0

try:
    i = 0
    pipe = a + b
    print(10 / i)
    print('завершено')
except ZeroDivisionError:
    print('Нельзя делить на 0')        # Ничего попадает первое исключение по ходу выполнения программы
except NameError:
    print('Нет переменных')     # Нет переменных

try:
    number = 10 / 0
except ZeroDivisionError as exc:
    print(f'Что-то не так - {exc}')        # Что-то не так - division by zero

try:
    number = 10 / 0
except ZeroDivisionError as exc:
    print(f'Что-то не так - {exc} c {exc.args}')        # Что-то не так - division by zero c ('division by zero',)


i = int(input('Введите число: '))

try:
    number = int(10 / i)
    print(number)

except (NameError, ZeroDivisionError) as exc:
    print(f'На ноль делить нельзя, класс ошибки {exc}, описание ошибки {exc.args}')

else:
    print('Не делили на ноль и это очень здорово')#  Если ошибки не было

finally:
    print('Дели на ноль или не дели я здесь')# всегда печатает




