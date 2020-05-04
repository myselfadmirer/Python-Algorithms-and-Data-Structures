# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных
# значения.


from random import randint

list_1 = [randint(-100, 100) for _ in range(31)]
print(f'Исходный список: {list_1}')
list_negative = [_ for _ in list_1 if _ < 0]
max_negative = None
for num in list_negative:
    if max_negative is None or num > max_negative:
        max_negative = num
print(f'Максимальный отрицательный элемент списка - {max_negative}, позиция в списке - {list_1.index(max_negative)}')
