# Найти максимальный элемент среди минимальных элементов столбцов матрицы.


from random import randint

m = int(input('Введите количество строк матрицы\n'))
n = int(input('Введите количество столбцов матрицы\n'))
matrix = [[randint(0, 20) for _ in range(n)] for _ in range(m)]
for line in matrix:
    for item in line:
        print(f'{item:4}', end='')
    print()
max_item = 0
for i in range(len(matrix[0])):
    min_item = matrix[0][i]
    for j in range(len(matrix)):
        if matrix[j][i] < min_item:
            min_item = matrix[j][i]
    if min_item > max_item:
        max_item = min_item
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы - {max_item}')
