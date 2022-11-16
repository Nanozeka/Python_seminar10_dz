# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]


import datetime
import time
from functools import wraps


# Декоратор таймер
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        finish = time.time_ns()
        print(finish - start)
        return res

    return wrapper


# Декоратор кэширования
def cacher(func):
    cach = {}

    @wraps(func)
    def wrapper(*args):
        key = args
        if key not in cach:
            cach[key] = func(*args)
        # print(cach)
        return cach[key]

    return wrapper


# Сама функция(с декораторами)
@timer
@cacher
def seq(n):
    result = []
    for i in range(n):
        res = (1 + i) **i
        result.append(res)
    return result    


def main():
    seq(10000)
    seq(10000)
    seq(10000)
    seq(10000)
    seq(10000)


if __name__ == '__main__':
    main()


# Результат выполнения функций:
# Я так понимаю,что 2,3,4,5 вычисления прошли вообще без затраты времени
# Просто взяли нужный результат и все
# 6896557000
# 0
# 0
# 0
# 0    