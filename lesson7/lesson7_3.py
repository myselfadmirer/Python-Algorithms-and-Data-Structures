# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы. Примечание: задачу можно решить без сортировки исходного массива. Но если
# это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также
# недопустима).


from random import randint


# Вариант без сортировки
def sort(array):
    for i in range(len(array)):
        count = 0
        left = right = 0
        for j in range(len(array)):
            if array[j] < array[i]:
                left += 1
            elif array[j] > array[i]:
                right += 1
            elif i == j:
                continue
            elif array[i] == array[j]:
                count += 1
        if right == left or abs(right - left) == count:
            return array[i]


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
# print(sort([2, 4, 8, 2, 0]))
# print(sort([4, 1, 33, 12, 15, 9, 5, 11, 9]))

if __name__ == '__main__':
    assert sort([2, 4, 8, 2, 0]) == 2, 'wrong'
    assert sort([4, 1, 33, 12, 15, 9, 5, 11, 9]) == 9, 'wrong'
