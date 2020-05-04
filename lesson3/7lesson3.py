# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
# минимальны), так и различаться.


from random import randint

list_1 = [randint(0, 100) for _ in range(21)]
print(f'Исходный список: {list_1}')
num_min1 = num_min2 = None
for num in list_1:
    if num_min1 is None or num_min1 > num:
        num_min2 = num_min1
        num_min1 = num
    elif num_min2 is None or num_min2 > num:
        num_min2 = num
print(f'Наименьший элемент списка - {num_min1}, следующий за ним элемент списка - {num_min2}')
