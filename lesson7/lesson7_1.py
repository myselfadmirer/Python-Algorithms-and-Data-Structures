# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.


from random import randint


# Алгоритм, представленный в видеоуроке:
def my_sort(array: iter):
    count = 1
    while count < len(array):
        for itm in range(len(array) - count):
            if array[itm] > array[itm + 1]:
                array[itm], array[itm + 1] = array[itm + 1], array[itm]
        count += 1
    print(f'my_sort {array}')


# my_sort([2, 5, 10, 18, 1, 8, 9, 0, 11, 7])"
# 1000 loops, best of 5: 65.6 usec per loop


my_list = [randint(-100, 99) for _ in range(10)]
# print(my_list)
my_sort(my_list)


# Вариант 2 алгоритма:
def my_sort2(array: iter):
    for i in range(len(array) - 1):
        for itm in range(len(array) - i - 1):
            if array[itm] > array[itm + 1]:
                array[itm], array[itm + 1] = array[itm + 1], array[itm]
    print(f'my_sort2 {array}')


# my_sort2([2, 5, 10, 18, 1, 8, 9, 0, 11, 7])"
# 1000 loops, best of 5: 63.3 usec per loop


my_list2 = [randint(-100, 99) for _ in range(10)]
# print(my_list2)
my_sort2(my_list2)

a = [24, -55, 22, 45, -76, -52, 69, 63, -4, -99]
# my_sort(a)
my_sort2(a)

if __name__ == '__main__':
    assert my_list == sorted(my_list), "wrong"
    assert my_list2 == sorted(my_list2), "wrong"
    assert a == sorted(a), "wrong"
