# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.


from random import randint

list_1 = [randint(0, 100) for _ in range(21)]
print(f'Исходный список: {list_1}')
ind_max = ind_min = 0
sum_el = 0
for i in range(len(list_1)):
    if list_1[i] > list_1[ind_max]:
        ind_max = i
    elif list_1[i] < list_1[ind_min]:
        ind_min = i
print(f'Максимальный элемент массива - {list_1[ind_max]}, минимальный - {list_1[ind_min]}')
if ind_max < ind_min:
    ind_min, ind_max = ind_max, ind_min
for num in list_1[ind_min + 1: ind_max]:
    sum_el += num
print(f'Сумма элементов между максимальным и минимальным равна {sum_el}')
