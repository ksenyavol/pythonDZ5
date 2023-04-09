# Задание 1. Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна
# запрашивать новые данные для вычислений. Завершение программы должно
# выполняться при вводе символа '0' в качестве знака операции. Если пользователь
# вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции
# Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.
# Подсказка:
# Вариант исполнения:
# - условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
# - условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
# Решите через рекурсию. В задании нельзя применять циклы
# Пример:
# Введите операцию (+, -, *, / или 0 для выхода): +
# Введите первое число: 214
# Введите второе число: 234
# Ваш результат 448
# Введите операцию (+, -, *, / или 0 для выхода): -
# Введите первое число: вп
# Вы вместо трехзначного числа ввели строку (((. Исправьтесь
# Введите операцию (+, -, *, / или 0 для выхода):


def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    else:
        return a / b


def is_correct_operation(operation):
    return operation == '0' or operation == '+' or operation == '-' or operation == '*' or operation == '/'


def get_operation():
    return input('Введите операцию: ')


def run_calculator(a=None, b=None):
    if a is None:
        a = float(input('Введите a: '))
    if b is None:
        b = float(input('Введите b: '))
    operation = get_operation()

    if not is_correct_operation(operation):
        print('Ошибка')
        run_calculator(a, b)
        return
    elif operation == '0':
        return
    elif operation == '/' and b == 0:
        print('На ноль делить нельзя')
        run_calculator()
        return
    else:
        print(calculate(a, b, operation))
        run_calculator()


run_calculator()

