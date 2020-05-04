# Определить, какое число в массиве встречается чаще всего.


from random import randint

list_1 = [randint(0, 100) for _ in range(21)]
print(f'Исходный список: {list_1}')
max_count = None
for num in set(list_1):
    if max_count is None or list_1.count(num) > list_1.count(max_count):
        max_count = num
print(f'Чаще всего в списке встреччается число {max_count}')

# Случайно написала сначала программу, которая находит несколько значений, если они встречаются одинаковое количество
# раз, и не захотела удалять.

max_count = 0
count = {}
for num in set(list_1):
    if list_1.count(num) > max_count:
        max_count = list_1.count(num)
        count.clear()
        count[num] = max_count
    elif list_1.count(num) == max_count:
        count[num] = max_count
print(f"Чаще всего в массиве встречается {', '.join(map(str, [key for key, value in count.items()]))}, число элементов "
      f"в исходном массиве - {max_count}")
