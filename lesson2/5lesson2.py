# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.


count = 0
for i in range(32, 128):
    count += 1
    print(f'{i} -> "{chr(i)}"', end=', ')
    if not count % 10:
        print('\n')
