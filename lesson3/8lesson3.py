# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.


matrix = [[int(input('Введите значение\n')) for _ in range(4)] for _ in range(4)]
for line in matrix:
    item_sum = 0
    for item in line:
        item_sum += item
        print(f'{item:4}', end='')
    line.append(item_sum)
    print(f'{item_sum:5}')
