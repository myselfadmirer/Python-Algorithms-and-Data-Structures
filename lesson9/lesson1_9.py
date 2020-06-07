# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается
# не решённой.

from hashlib import sha1


def hash_func(s: str) -> int:
    assert len(s) > 0, 'Строка не может быть пустой'
    substring_set = set()
    for len_substr in range(1, len(s)):
        for i in range(len(s) - len_substr + 1):
            sub_str = sha1(s[i:i + len_substr].encode('utf-8')).hexdigest()
            substring_set.add(sub_str)
    print(substring_set)
    return len(substring_set)


if __name__ == '__main__':
    string = input('Введите строку\n')
    print(hash_func(string))
