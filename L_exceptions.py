print('Создание исключений')
print('Example 1 - поднимаем общее (Exception) исключения и завершаем программу, если оно возникает, наше описание')


def greet_person(name):
    if name == 'Bad guy':
        raise Exception('Go away in red')
    print(f'Welcome {name}')


greet_person('Oleg')
# greet_person('Bad guy')  # функция вызывает исключение с сообщением "Go away". В противном случае она просто выводит
# приветствие. При вызове greet_person('Bad guy') это приведет к выбросу исключения, и программа завершится, если не
# будет перехвачено в блоке try/except

# Traceback (most recent call last):
#   File "D:\PythonProjectUni\Module_08\L_exceptions.py", line 9, in <module>
#     greet_person('Bad guy')
#   File "D:\PythonProjectUni\Module_08\L_exceptions.py", line 5, in greet_person
#     raise Exception('Go away')
# Exception: Go away


print('Example 2 - вызываем конкретное исключение NameError вручную')
'''
try:
    raise NameError('Go away')
except NameError as exc:                                        # объявляем тип и аргумент
    print(f'Исключение типа {type(exc)}, описание {exc.args}')  # выводим тип и аргумент ошибки
    raise
'''
# В этом случае вы вызываете исключение NameError вручную, затем ловите его с помощью блока except. Внутри блока
# except вы можете обрабатывать исключение (в данном случае просто выводите информацию о нем) и затем с помощью raise
# повторно выбрасываете то же исключение, что позволяет передать его дальше в стек вызовов.

# Исключение типа <class 'NameError'>, описание ('Go away',)
# Traceback (most recent call last):
#   File "D:\PythonProjectUni\Module_08\L_exceptions.py", line 21, in <module>
#     raise NameError('Go away')
# NameError: Go away

# Цель кода:
# - Первый фрагмент кода демонстрирует простую проверку передачи данных и выброс исключения при некорректных данных.
# - Второй фрагмент — это более сложная обработка исключений, когда необходимо вывести информацию о самом исключении и,
# возможно, продолжить выполнение программы (при желании) после его обработки.

print('Example 3 собственные исключения')


class ProZero(Exception):
    pass


def f(a, b):
    if b == 0:
        raise ProZero('Не делить на ноль')
    return a // b


print(f(5, 1))
# print(f(5, 0))
# Traceback (most recent call last):
#   File "D:\PythonProjectUni\Module_08\L_exceptions.py", line 56, in <module>
#     print(f(5, 0))
#           ^^^^^^^
#   File "D:\PythonProjectUni\Module_08\L_exceptions.py", line 52, in f
#     raise ProZero('Не делить на ноль')
# ProZero: Не делить на ноль

print('Example 4 - все вместе')


class ProZero(Exception):

    def __init__(self, message, mess_info):
        self.message = message
        self.mess_info = mess_info

def f(a, b):
    if b == 0:
        raise ProZero('Нельзя делить на ноль', {'a': a, 'b': b})
    return a // b


try:                             # если бы не try and except, то была бы просто ошибка, а так мы исключение перехватили
    result = f(5, 0)
except ProZero as exc:
    print('Возникла ошибка')
    print(f'Класс: {exc.message}, Описание: {exc.mess_info}')

# Возникла ошибка
# Класс: Нельзя делить на ноль, Описание: {'a': 5, 'b': 0}

print('Example 5 - chatGPT')
class ProZero(Exception):
    def __init__(self, message, mess_info):
        super().__init__(message)  # Вызов конструктора базового класса
        self.message = message
        self.mess_info = mess_info

def f(a, b):
    if b == 0:
        raise ProZero('Нельзя делить на ноль', {'a': a, 'b': b})
    return a // b

try:
    result = f(5, 0)
except ProZero as exc:
    print('Возникла ошибка')
    print(f'Класс: {exc.message}, Описание: {exc.mess_info}')

print('Вебинар 23.09')
def f1():
    try:
        f2()
    except ValueError as e:
        print(f'Перехвачено в функции 1 {e}')
        raise
def f2():
    try:
        f3()
    except ValueError as e:
        print(f'Перехвачено в функции 2 {e}')
        raise

def f3():
    raise ValueError('Ошибка в функции 3')

try:
    f1()
except ValueError as e:
    print(f'Исключение перехвачено {e}')

# Принцип LIFO (Last In, First Out): Последний шанс перехватить это try f1, до этого f1 и ближайший к ошибке f2
# - LIFO означает, что последняя добавленная функция (в данном случае f3) будет первой, которая завершает выполнение.
# То есть, когда происходит исключение в f3(), оно "поднимается" вверх по стеку вызовов к f2(), затем к f1().
# - Когда происходят исключения, управление передается обратно по стеку вызовов, и если исключение не обработано
# (например, не перехвачено блоком try/except), программа завершает свою работу с выводом информации об ошибке.
# ### Обработка исключений
# В данном примере, исключение ValueError выбрасывается в f3(), и поскольку оно не обработано там, управление
# возвращается к f2(), затем к f1(). Вызвав f1(), программа попадает в блок try, где происходит перехват исключения.

print('Создание исключений')

class MyError(Exception):
    pass

def func():
    raise MyError('Мое исключение')

try:
    func()
except MyError as e:
    print(f'Перехватили ... {e}')

print('Создание исключений с атрибутами')

class MyError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

try:
    raise MyError('Ошибка с кодом:', 404)
except MyError as e:
    print(f'Перехватили ... {e} и код ошибки: {e.code}')



print('Создание исключений с атрибутами и функцией')
class MyError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

def func():
    raise MyError('Ошибка с кодом:', 404)

try:
    func()
except MyError as e:
    print(f'Перехватили ... {e} и код ошибки: {e.code}')

# В приведенном коде строка super().__init__(message) выполняет вызов конструктора родительского класса Exception
# с аргументом message. Давайте подробнее рассмотрим, что это означает и зачем вам это нужно.
# ### Роль super().__init__(message)
# 1. Инициализация родительского класса: Когда вы создаете свой собственный класс исключений (в вашем случае, MyError),
# вы часто хотите, чтобы он наследовал поведение и функциональность уже существующего класса исключений, например,
# Exception. У класса Exception есть свой собственный механизм обработки сообщений об ошибках, который вы, как правило,
# хотите перенести в свой класс.
# 2. Хранение сообщения об ошибке: Когда вы вызываете super().__init__(message), это передает message конструктору
# родительского класса Exception, который хранит это сообщение в своём внутреннем состоянии. Это позволяет вам
# использовать стандартные методы обработки исключений, такие как str(e) или repr(e), чтобы получить сообщение
# об ошибке, когда вы перехватываете исключение MyError.
# 3. Повышение совместимости: Если вы используете стандартные механизмы, такие как try-except, то перехват исключений
# будет работать корректно, и по ним можно будет получить сообщение об ошибке.
# ### Пример кода
# Если бы вы не вызвали super().__init__(message), и просто в вашем классе MyError было бы только self.code = code,
# то сообщение об ошибке было бы недоступно при перехвате этого исключения. Если вы потом попробуете вывести str(e)
# или просто print(e), где e — это MyError, ничего полезного не получится, поскольку механизм по умолчанию не
# будет знать, как обрабатывать ваше собственное исключение.

print('Что будет без super()')

class MyError(Exception):
    def __init__(self, message, code):
        self.code = code  # нет super().__init__(message)

try:
    raise MyError('Ошибка с кодом:', 404)
except MyError as e:
    print(f'Перехватили ... {e} и код ошибки: {e.code}')  # Это будет напечатать что-то неинформативное, например, "<__main__.MyError object at 0x...>"

# Перехватили ... ('Ошибка с кодом:', 404)

print('Что будет без super(), но с self.message = message')
class MyError(Exception):
    def __init__(self, message, code):
        self.code = code  # нет super().__init__(message)
        self.message = message

try:
    raise MyError('Ошибка с кодом:', 404)
except MyError as e:
    print(f'Перехватили ... {e} и код ошибки: {e.code}')  # Это будет напечатать что-то неинформативное, например, "<__main__.MyError object at 0x...>"

# Перехватили ... ('Ошибка с кодом:', 404)

print('Создание исключений с атрибутами и функцией пример')

class InvAge(Exception):
    def __init__(self, age, message = 'Ошибка в значении возраста'):
        self.age = age
        self.message = message
        super().__init__(self.message)

def set_age(age):
    if age < 0:
        raise InvAge(age)
    print(f'Возраст был установлен {age}')

try:
    set_age(int(input('Введите свой возраст: ')))
except InvAge as e:
    print(f'{e.message}. Указан возраст {e.age}')

print('Логирование и подключение')




