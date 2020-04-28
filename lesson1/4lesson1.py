# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

a = input('Введите первую букву: \n')
b = input('Введите вторую букву: \n')
if a.lower() > b.lower():
    a, b = b, a
num_a = ord(a.lower()) - 96
num_b = ord(b.lower()) - 96
letter_between = num_b - num_a - 1
print(f'Номер буквы {a} - {num_a}, номер буквы {b} - {num_b}, между ними {letter_between} букв(а/ы)')
