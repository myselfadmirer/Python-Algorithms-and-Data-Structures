# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы. Примечание: задачу можно решить без сортировки исходного массива. Но если
# это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также
# недопустима).


from random import randint


# Вариант без сортировки
def sort(array):
    i = 0
    while i < len(array):
        left = right = 0
        mid = array[i]
        for elem in array:
            if elem > mid:
                right += 1
            elif elem is mid:
                continue
            else:
                left += 1
        if right == left:
            return mid
        else:
            i += 1


# Применена шейкерная сортировка (в условии задачи сказано, что можно сортировать, но методом, которого не было
# на лекции). На всякий случай исходный массив не менялся.
def mid_shaker(array: iter):
    shake_list = array[:]
    flag = True
    left_ind = 0
    right_ind = len(shake_list) - 1
    while flag:
        flag = False
        for i in range(left_ind, right_ind):
            if shake_list[i] > shake_list[i + 1]:
                shake_list[i], shake_list[i + 1] = shake_list[i + 1], shake_list[i]
                flag = True
        if not flag:
            break
        flag = False
        right_ind -= 1
        for i in range(right_ind - 1, left_ind - 1, -1):
            if shake_list[i] > shake_list[i + 1]:
                shake_list[i], shake_list[i + 1] = shake_list[i + 1], shake_list[i]
                flag = True
        left_ind += 1
    return shake_list[len(array) // 2]


m = int(input('m = '))
n = 2 * m + 1
my_list = [randint(-100, 100) for _ in range(n)]
print(my_list)
print(sorted(my_list))
print(f'Функция sort: {sort(my_list)}')
print(f'Функция mid_shaker: {mid_shaker(my_list)}')
