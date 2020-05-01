# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.

n = int(input('Введите количество вводимых чисел: \n'))
max_num = 0
sum_num = 0
for i in range(n):
    num = int(input('Введите число: \n'))
    calc = num
    mid_sum = 0
    while calc != 0:
        mid_sum += calc % 10
        calc //= 10
    if mid_sum > sum_num:
        sum_num = mid_sum
        max_num = num
print(f'Максимальная сумма цифр {sum_num} принадлежит числу {max_num}')
