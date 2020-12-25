"""
Cпринт 13, Задача B, ревью 2
Матаков Денис
dmatakov@yandex.ru

Алла ошиблась со структурой данных. Она решила хранить массив в кольцевом буфере.
Проблема в том, что массив был отсортирован. И в нем можно было искать элемент
за логарифмическое время. Алла скопировала данные из кольцевого буфера в обычный
массив. Но он больше не является отсортированным. Тем не менее нужно обеспечить
возможность находить в нем элемент за O(log n).

Сортировать массив нельзя.
Объем дополнительной памяти, помимо массива, в который считываются данные, и стека \
вызовов функций, O(1). Использование сетов, словарей, вспомогательных массивов запрещено


15 дек 2020, 13:19:12
45505770
51ms
3.95Mb
"""


def search(corrupted_buffer, left, right, search_number):
    if left > right:
        return -1

    middle = (left + right) // 2
    if corrupted_buffer[middle] == search_number:
        return middle

    # Проверка, вдруг отсортирована левая часть
    if corrupted_buffer[left] <= corrupted_buffer[middle]:

        # Запускаем бинарный поиск
        if corrupted_buffer[left] <= search_number <= corrupted_buffer[middle]:
            return search(corrupted_buffer, left, middle - 1, search_number)
        return search(corrupted_buffer, middle + 1, right, search_number)

    # Если отсортирована вторая часть
    if corrupted_buffer[middle] <= search_number <= corrupted_buffer[right]:
        return search(corrupted_buffer, middle + 1, right, search_number)
    return search(corrupted_buffer, left, middle - 1, search_number)


if __name__ == "__main__":
    _ = input()
    number = int(input())
    buffer = [int(i) for i in input().split()]
    index = search(buffer, 0, len(buffer) - 1, number)
    print(index)
