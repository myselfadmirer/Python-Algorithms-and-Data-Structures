# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a, b, c = map(int, input('Введите в строку 3 целых числа a, b, c: \n').split())
if a < b:
    a, b = b, a
if c > b:
    if c > a:
        a, b, c = c, a, b
    else:
        b, c = c, b
print(f'Среднее число - {b}')
