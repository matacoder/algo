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


def compile_biggest_number(lst):
    """
    Compile biggest number
    :param numbers: Array of numbers as strings
    :return: Number as string
    """
    return ''.join(sorted(lst,
                          key=functools.cmp_to_key(lambda a, b: (int(b + a) > int(a + b)) - (int(b + a) < int(a + b)))))


if __name__ == "__main__":
    _ = input()
    data = compile_biggest_number(input().split())
    print(data)
