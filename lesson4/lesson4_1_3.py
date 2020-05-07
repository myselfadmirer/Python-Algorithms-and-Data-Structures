# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков.
# Условие задачи: В диапазоне натуральных чисел от 2 до n (заменено для вориативности) определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# В файлах 1_1lesson4.py, 1_2lesson4.py, 1_3lesson4.py
# пердставлено 3 разных алгоритма решения задачи.
# Вариант 3: с использованием временной переменной для фиксации результатов вычисления и выводом объекта-генератора.

import cProfile


def my_func(n):
    for i, value in enumerate(range(2, 10), start=2):
        spam = 0
        for num in range(2, n):
            if not num % value:
                spam += 1
        yield f'Цифре {i} кратно {spam} чисел в диапазоне от 2 до 99'

# Результаты timeit:

# my_func(10)
# 1000 loops, best of 5: 1.09 usec per loop

# my_func(100)
# 1000 loops, best of 5: 1.18 usec per loop

# my_func(1000)
# 1000 loops, best of 5: 1.25 usec per loop

# my_func(10000)"
# 1000 loops, best of 5: 1.25 usec per loop

# Результаты cProfile:

# cProfile.run('my_func(10)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 lesson4_1_3.py:12(my_func)

# cProfile.run('my_func(100)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 lesson4_1_3.py:12(my_func)

# cProfile.run('my_func(1000)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 lesson4_1_3.py:12(my_func)

# cProfile.run('my_func(10000)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 lesson4_1_3.py:12(my_func)

# В результе исследования можно сделать вывод, что самым затратным методом расчета является алгоритм с использованием
# словаря. Далее идет список, а после - генератор, его сложность можно определить как O(1), так как при изменении
# количества объектов, время на выполнение задачи практически не меняется. При этом сложность 2 других - O(n) и
# зависимость линейная, но время выполнения зависит от количества объектов. Обращаю внимание, что не считалось время
# время вывода результата, которое у объекта-генератора может быть больше.