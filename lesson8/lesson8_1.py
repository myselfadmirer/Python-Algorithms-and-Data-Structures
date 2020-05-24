# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.


# Создание матрицы смежности.
def my_handshakes(x):
    friends = []
    handshakes = 0
    for i in range(x):
        friend = []
        for j in range(x):
            if j == i:
                friend.append(0)
            else:
                if j > i:  # считаются только уникальные рукопожатия
                    handshakes += 1
                friend.append(1)
        friends.append(friend)
    # print(*friends, sep='\n')
    print(f'Сумма рукопожатий - {handshakes}')


# Используется только половина матрицы, так как матрица получается симметричной
def my_handshakes2(x):
    friends = []
    for i in range(x):
        handshake = []
        for j in range(i + 1, x):  # считаются только уникальные рукопожатия
            handshake.append(1)
        friends.append(handshake)
    # print(*friends, sep='\n')
    print(f'Сумма рукопожатий {x} друзей - {sum([sum(friend) for friend in friends])}')


n = int(input('n = '))
my_handshakes(n)
my_handshakes2(n)

if __name__ == '__main':
    assert my_handshakes(20) == 190, 'wrong'
    assert my_handshakes2(20) == 190, 'wrong'
