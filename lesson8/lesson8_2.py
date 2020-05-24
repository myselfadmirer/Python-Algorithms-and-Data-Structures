# Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.


from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    first_vertex = start
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    ways = {}
    for v, point in enumerate(parent):
        way = deque()
        i = v
        while parent[i] != -1:
            way.appendleft(parent[i])
            i = parent[i]
        if len(way) > 0:
            way.append(v)
            ways[v] = way
        elif v == first_vertex:
            ways[v] = 'Начало пути'
        else:
            ways[v] = 'Нет пути'

    return cost, ways


s = int(input('От какой вершины идти: '))
min_cost_way, shortest_ways = dijkstra(g, s)

for v, w in shortest_ways.items():
    if s == v:
        print(f'Вершина {v} - Начало пути')
    elif w == 'Нет пути':
        print(f'Невозможно попасть в вершину {v}')
    else:
        print(
            f"Кратчайший путь от вершины {s} до вершины {v} - {'->'.join(map(str, w)):13}| "
            f"минимальная стоимость пути = {min_cost_way[v]}")
