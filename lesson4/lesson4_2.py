# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
# улучшить/оптимизировать под задачу. Второй — без использования «Решета Эратосфена». Примечание. Вспомните
# классический способ проверки числа на простоту.

# Вывод: функция sieve_f имеет сложность O(n^2), функция prime_f имеет сложность O(2^n).

# import cProfile

# Поиск с помощью алгоритма «Решето Эратосфена»


def sieve_f(n):
    end = n
    while True:
        sieve = [i for i in range(end)]
        if end > 1:
            sieve[1] = 0
        for i in range(2, end):
            if sieve[i] != 0:
                j = i * 2
                while j < end:
                    sieve[j] = 0
                    j += i
        result = [i for i in sieve if i != 0]
        if len(result) >= n:
            return result[n - 1]
        end *= 2


# sieve_f(1)"
# 1000 loops, best of 5: 8.1 usec per loop

# sieve_f(5)"
# 1000 loops, best of 5: 33.3 usec per loop

# sieve_f(50)"
# 1000 loops, best of 5: 567 usec per loop

# sieve_f(150)"
# 1000 loops, best of 5: 1.75 msec per loop

# sieve_f(500)"
# 1000 loops, best of 5: 6.25 msec per loop

# cProfile.run('sieve_f(1)')
# 13 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 lesson4_2.py:14(sieve_f)

# cProfile.run('sieve_f(5)')
# 13 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 lesson4_2.py:14(sieve_f)

# cProfile.run('sieve_f(50)')
# 16 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 lesson4_2.py:14(sieve_f)

# cProfile.run('sieve_f(150)')
# 16 function calls in 0.002 seconds
# 1    0.001    0.001    0.002    0.002 lesson4_2.py:14(sieve_f)

# cProfile.run('sieve_f(500)')
# 16 function calls in 0.007 seconds
# 1    0.005    0.005    0.007    0.007 lesson4_2.py:14(sieve_f)

# Поиск наименьшего делителя с помощью квадратного корня числа


def prime_f(n):
    end = n
    while True:
        result = [2]
        for a in range(3, end, 2):
            i = int(a ** 0.5)
            while 1 < i <= a ** 0.5:
                if a % i == 0:
                    break
                else:
                    i -= 1
            else:
                result.append(a)
                if len(result) >= n:
                    return result[n - 1]
        end *= 2


# prime_f(1)"
# 1000 loops, best of 5: 2.9 usec per loop

# prime_f(5)"
# 1000 loops, best of 5: 16.5 usec per loop

# prime_f(50)"
# 1000 loops, best of 5: 1.29 msec per loop

# prime_f(150)"
# 1000 loops, best of 5: 7.78 msec per loop

# prime_f(500)"
# 1000 loops, best of 5: 56.8 msec per loop

# cProfile.run('prime_f(1)')
# 6 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 lesson4_2.py:69(prime_f)

# cProfile.run('prime_f(5)')
# 20 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 lesson4_2.py:69(prime_f)

# cProfile.run('prime_f(50)')
# 268 function calls in 0.001 seconds
# 1    0.001    0.001    0.001    0.001 lesson4_2.py:69(prime_f)

# cProfile.run('prime_f(150)')
# 708 function calls in 0.008 seconds
# 1    0.007    0.007    0.008    0.008 lesson4_2.py:69(prime_f)

# cProfile.run('prime_f(500)')
# 2128 function calls in 0.070 seconds
# 1    0.069    0.069    0.070    0.070 lesson4_2.py:69(prime_f)

# while True:
#     x = int(input('x = '))
#     if x == 0:
#         break
#     print(sieve_f(x))
#     print(prime_f(x))

# assert sieve_f(4) == 7
# assert prime_f(80) == 409


# Var2 prime_f2 медленнее варианта 1:

def prime_f2(n):
    end = n
    result = []
    while len(result) < n:
        result = [2]
        for a in range(3, end, 2):
            i = int(a ** 0.5)
            while 1 < i <= a ** 0.5:
                if a % i == 0:
                    break
                else:
                    i -= 1
            else:
                result.append(a)
        end *= 2
    return result[n - 1]

# prime_f2(1)"
# 1000 loops, best of 5: 3.1 usec per loop
#
# prime_f2(5)"
# 1000 loops, best of 5: 63.9 usec per loop
#
# prime_f2(50)"
# 1000 loops, best of 5: 4.58 msec per loop
