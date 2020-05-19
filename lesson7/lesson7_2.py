# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


from random import uniform


def my_sort(array: iter):
    if len(array) < 2:
        return array
    left = my_sort(array[:len(array) // 2])
    right = my_sort(array[len(array) // 2:])
    i = j = 0
    result = []
    while len(left) > i or len(right) > j:
        if len(left) <= i:
            result.append(right[j])
            j += 1
        elif len(right) <= j:
            result.append(left[i])
            i += 1
        elif right[j] > left[i]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
    return result


my_list = [uniform(0, 50).__round__(3) for _ in range(10)]
print(my_list)
a = my_sort(my_list)
print(a)
