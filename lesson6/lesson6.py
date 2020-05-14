# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти. Примечание:
# По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть); проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде
# комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.

import sys

# Версия Python и Windows: 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] win32

# Задача 2.9
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.


# Вариант 1.
# Временные переменные, приведение входных данных к типу int.

# num_list = list(map(int, input('Введите числа через пробел\n').split()))
# max_num = 0
# sum_num = 0
# for num in num_list:
#     calc = num
#     mid_sum = 0
#     while calc != 0:
#         mid_sum += calc % 10
#         calc //= 10
#     if mid_sum > sum_num:
#         sum_num = mid_sum
#         max_num = num
# print(f'Вариант 1. Максимальная сумма цифр {sum_num} принадлежит {max_num}')

# Вариант 2.
# Временные переменные, входные данные типа str.

# num_list = list(input('Введите числа через пробел\n').split())
# max_num = 0
# sum_num = 0
# for itm in num_list:
#     mid_sum = 0
#     for i in itm:
#         mid_sum += int(i)
#         if mid_sum > sum_num:
#             sum_num = mid_sum
#             max_num = itm
# print(f'Вариант 2. Максимальная сумма цифр {sum_num} принадлежит {max_num}')

# Вариант 3. Сохранение всех значений сумм в словарь и поиск максимального значения по словарю.

# num_list = list(input('Введите числа через пробел\n').split())
# result = dict.fromkeys(num_list, 0)
# for itm in num_list:
#     mid_sum = 0
#     for i in itm:
#         mid_sum += int(i)
#     result[itm] = mid_sum
# sum_num = max(result.values())
# max_num = [i[0] for i in result.items() if i[1] == sum_num]
# print(f"Вариант 3. Максимальная сумма цифр {sum_num} принадлежит {''.join(max_num)}")

# Вариант 4. Приведен здесь для сравнения в качестве примера оптимизации Варианта 3.

# num_list = list(map(int, input('Введите числа через пробел\n').split()))
# result = dict.fromkeys(num_list, 0)
# for num in num_list:
#     calc = num
#     mid_sum = 0
#     while calc != 0:
#         mid_sum += calc % 10
#         calc //= 10
#     result[num] = mid_sum
# sum_num = max(result.values())
# max_num = [i[0] for i in result.items() if i[1] == sum_num]
# print(f"Вариант 4. Максимальная сумма цифр {sum_num} принадлежит {''.join(map(str, max_num))}")


# Вывод. Во всех трех случаях имеются переменные max_num, max_sum b mid_sum и список значений num_list.
# В первых двух случаях идет переприсвоение значений, в третьем - все значения mid_sum вносятся в словарь с
# ключом - число из входных данных.
# ПРИМЕР для проверки (список входных значений для всех трех случаев): 11 34 56 12 80 10.
# Максимальная сумма цифр 11 принадлежит 56

# Создаем копию словаря locals(), схраниящего все переменные. Копия хранит только переменные программы,
# так как создана до программы проверки. Если создать ее позже или использовать сам словарь locals(), то в него будут
# добавлены также переменные функции подсчета и вывода результатов.
local_var_dict = locals().copy()


# Функция вычисления использованной переменной памяти.
def get_size_var(x, level=0):
    res = sys.getsizeof(x)
    # print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, '__items__'):
            for xx in x.items():
                res += get_size_var(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                res += get_size_var(xx, level + 1)
    return res


result_size = 0
print(local_var_dict)
# Проходимся по словарю с переменными
for var in local_var_dict.keys():
    result_size += get_size_var(local_var_dict[var])

print(result_size)

# РЕЗУЛЬТАТЫ:
# Вариант 1
# Переменные: {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0092AF58>, '__spec__': None,
# '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:/Users/NELYUBINA/git-project/Python-Algorithms-and-Data-Structures/lesson6/lesson6.py',
# '__cached__': None, 'sys': <module 'sys' (built-in)>, 'num_list': [11, 34, 56, 12, 80, 10], 'max_num': 56,
# 'sum_num': 11, 'num': 10, 'calc': 0, 'mid_sum': 1}
# Использовано памяти: 541 b

# РЕЗУЛЬТАТЫ:
# Вариант 2
# Переменные: {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0101AF58>, '__spec__': None,
# '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:/Users/NELYUBINA/git-project/Python-Algorithms-and-Data-Structures/lesson6/lesson6.py',
# '__cached__': None, 'sys': <module 'sys' (built-in)>, 'num_list': ['11', '34', '56', '12', '80', '10'],
# 'max_num': '56', 'sum_num': 11, 'itm': '10', 'mid_sum': 1, 'i': '0'}
# Использовано памяти: 635 b

# РЕЗУЛЬТАТЫ:
# Вариант 3
# Переменные: {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00BCAF58>, '__spec__': None,
# '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:/Users/NELYUBINA/git-project/Python-Algorithms-and-Data-Structures/lesson6/lesson6.py',
# '__cached__': None, 'sys': <module 'sys' (built-in)>, 'num_list': ['11', '34', '56', '12', '80', '10'],
# 'result': {'11': 2, '34': 7, '56': 11, '12': 3, '80': 8, '10': 1}, 'itm': '10', 'mid_sum': 1, 'i': '0',
# 'sum_num': 11, 'max_num': ['56']}
# Использовано памяти: 1037 b

# РЕЗУЛЬТАТЫ:
# Вариант 4
# Переменные: {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x014EAF58>, '__spec__': None,
# '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:/Users/NELYUBINA/git-project/Python-Algorithms-and-Data-Structures/lesson6/lesson6.py',
# '__cached__': None, 'sys': <module 'sys' (built-in)>, 'num_list': [11, 34, 56, 12, 80, 10],
# 'result': {11: 2, 34: 7, 56: 11, 12: 3, 80: 8, 10: 1}, 'num': 10, 'calc': 0, 'mid_sum': 1, 'sum_num': 11,
# 'max_num': [56]}
# Использовано памяти: 865 b

# ВЫВОД.
# Работа с типом int занимает меньше памяти, не смотря на перевод в int с помощью map всего списка num_list (Вариант 1).
# Работа со строками не требует вычислений в данной задаче, но использует больше памяти (Вариант 2). Третий метод с
# сохранением всех сумм в словарь менее грмоздкий, не требует пересохранения и введения временных переменных
# (Вариант 3), но требоует больше памяти, относительно Варианта 1, в 2 раза. Оптимизировать Вариант 3 можно с помощью
# приведения входных данных к типу int (Вариант 4).
