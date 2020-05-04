# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.


values = dict.fromkeys(range(2, 10), 0)
for key, value in values.items():
    for num in range(2, 100):
        if num % key == 0:
            values[key] += 1
    print(f'Числу {key} кратно {values[key]} чисел в диапазоне от 2 до 99')
