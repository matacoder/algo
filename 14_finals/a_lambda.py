"""
Cпринт 14, Задача А, ревью 1
Матаков Денис
dmatakov@yandex.ru

Даны числа. Нужно определить, какое самое большое число можно из них составить.

28 дек 2020, 17:08:35
45960605
A
Python 3.7.3
OK
-
54ms
3.93Mb
"""
import functools


def comparator(a, b):
    ab = int(a + b)
    ba = int(b + a)
    if ab > ba:
        return -1
    elif ab < ba:
        return 1
    return 0


def compile_biggest_number(numbers):
    """
    Compile biggest number
    :param numbers: Array of numbers as strings
    :return: Number as string
    """
    numbers = sorted(numbers, key=lambda arr: arr[0::1], reverse=True)
    # print(numbers)
    return ''.join(numbers)


if __name__ == "__main__":
    _ = input()
    data = compile_biggest_number(input().split())
    print(data)
