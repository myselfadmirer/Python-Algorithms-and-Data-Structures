# Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

from random import randint


# Граф с псевдослучайной последовательностью соединения вершин
def graph_func(x):
    points = []
    for i in range(x):
        point = set()
        num = randint(1, n // 2)  # Для наглядности количество исходящих ребер равно половине количества вершин
        while len(point) < num:
            spam = randint(0, n - 1)
            if spam != i:
                point.add(spam)
        points.append(point)
    return points


n = int(input('n = '))
point_list = graph_func(n)
print(point_list)


def search_func(start, visited, prev, my_list):
    visited[start] = True
    for i in my_list[start]:
        if not visited[i]:
            prev[i] = start
            search_func(i, visited, prev, my_list)


is_visited = [False] * n
prev_elem = [None] * n
first = int(input(f'Вершина начала обхода от 0 до {n - 1} - '))
search_func(first, is_visited, prev_elem, point_list)
for v, elem in enumerate(
        is_visited):  # Список вершин, которые обошел алгоритм (True для посещенных, False для недоступных)
    print(f'Вершина {v} посещена - {"Да" if elem == True else "Нет"}')
