# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


from random import randint

list_1 = [randint(0, 100) for _ in range(21)]
print(f'Исходный список: {list_1}')
ind_max = ind_min = None
for i in range(len(list_1)):
    if ind_min is None or list_1[i] < list_1[ind_min]:
        ind_min = i
    elif ind_max is None or list_1[i] > list_1[ind_max]:
        ind_max = i
print(f'Максимальное значение списка: {list_1[ind_max]}, минимальное значение списка: {list_1[ind_min]}.')
list_1[ind_min], list_1[ind_max] = list_1[ind_max], list_1[ind_min]
print(f'   Новый список: {list_1}')
