# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import deque, namedtuple, Counter


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf:
    def __init__(self, char):
        self.char = char

    def walk(self, code, acc):
        code[self.char] = acc


def huffman_encode(s):
    counter = []
    i = 1
    for ch, freq in Counter(s).items():
        counter.append((freq, i, Leaf(ch)))
        i += 1
    count = 0
    while len(counter) > 1:
        counter.sort(reverse=True)
        print(counter)
        freq1, _count1, left = counter.pop()
        freq2, _count2, right = counter.pop()
        counter.append((freq1 + freq2, count, Node(left, right)))
        count -= 1
    code = dict()
    root = counter[0][2]
    root.walk(code, '')
    return code
    # return counter


def main():
    s = input('String to encode\n')
    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')
    print(code, '\n', encoded)


if __name__ == '__main__':
    main()
