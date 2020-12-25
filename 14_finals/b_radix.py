"""
Cпринт 14, Задача B, ревью 1
Матаков Денис
dmatakov@yandex.ru

Алгоритм поразрядной сортировки

24 дек 2020, 13:33:44
45837599
B
Python 3.7.3
OK
-
476ms
9.59Mb
"""


def counting_sort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


def radix_sort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        counting_sort(array, place)
        place *= 10


if __name__ == "__main__":
    _ = input()
    data = [int(i) for i in input().split()]

    radix_sort(data)
    data = [str(i) for i in data]
    print(' '.join(data))
