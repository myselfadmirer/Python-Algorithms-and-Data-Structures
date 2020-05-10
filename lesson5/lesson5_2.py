# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел
# из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому
# использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

from collections import deque

values = '0123456789ABCDEF'


def adding_func(m, n):
    global values
    c = deque()
    rest = 0
    for k in range(1, len(n) + 1):
        temp = values.index(m[-k]) + values.index(n[-k])
        c.appendleft(values[(temp + rest) % 16])
        rest = (temp + rest) // 16
    for k in range(len(m) - len(n)):
        temp = values.index(m[k])
        c.appendleft(values[(temp + rest) % 16])
        rest = (temp + rest) // 16
    if rest > 0:
        c.appendleft(values[rest])
    return c


while True:
    operation = input('Введите +, * или q для выхода:\n')
    try:
        if operation not in {'+', '*', 'q'}:
            raise ValueError
    except ValueError as e:
        print('Неверный знак операции!')
        continue
    if operation == 'q':
        break
    a = input('Введите первое число в 16-ричной системе счисления:\n')
    b = input('Введите второе число в 16-ричной системе счисления:\n')
    a = deque(a.upper())
    b = deque(b.upper())
    if len(a) < len(b):
        a, b = b, a
    result = deque()
    if operation == '+':
        result = adding_func(a, b)
        print(f"{''.join(a)} + {''.join(b)} = {''.join(result)}")
    else:
        spam_sum_2 = deque()
        spam_sum = deque()
        for i in range(1, len(b) + 1):
            rest_num = 0
            if i - 1 > 0:
                for _ in range(i - 1):
                    spam_sum.append('0')
            for j in range(1, len(a) + 1):
                spam = values.index(b[-i]) * values.index(a[-j])
                spam_sum.appendleft(values[(spam + rest_num) % 16])
                rest_num = (spam + rest_num) // 16
            if rest_num > 0:
                spam_sum.appendleft(values[rest_num])
            if i - 1 > 0:
                result = adding_func(spam_sum, spam_sum_2)
                spam_sum_2 = result.copy()
                spam_sum.clear()
            else:
                spam_sum_2 = spam_sum.copy()
                spam_sum.clear()
        # assert result == deque(['7', '1', 'B', '8', 'E', '4'])
        print(f"{''.join(a)} * {''.join(b)} = {''.join(result)}")

# assert adding_func('C4F', 'A2') == deque(['C', 'F', '1'])
