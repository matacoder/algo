"""
Cпринт 14, Задача А, ревью 1
Матаков Денис
dmatakov@yandex.ru

Даны числа. Нужно определить, какое самое большое число можно из них составить.

24 дек 2020, 13:47:23
45838206
A
Python 3.7.3
OK
-
43ms
4.19Mb

"""


def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return (int(ba) > int(ab)) - (int(ba) < int(ab))


def compare(mycmp):
    # Convert a cmp= function into a key= function
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


if __name__ == "__main__":
    _ = input()
    a = input().split()
    a = [int(i) for i in a]
    sorted_array = sorted(a, key=compare(comparator))
    number = "".join([str(i) for i in sorted_array])
    print(number)
