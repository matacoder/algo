"""
Cпринт 15, Задача A, ревью 1
Матаков Денис
dmatakov@yandex.ru

Heap sort (пирамидальная сортировка)

25 дек 2020, 10:48:41
45871236
A
Python 3.7.3
OK
-
425ms
31.55Mb
"""


# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def is_kondratiy(player_name):
    for char in 'kondratiy':
        if char not in player_name:
            if char.upper() not in player_name:
                return False
    return True


if __name__ == "__main__":
    lines = int(input())

    players_sums = {}  # словарь с ключами-очками и значениями-строками ввода
    players_stack = []  # здесь будет стэк с игроками в порядке появления
    kondratiy_stack = []  # здесь будем держать Кондратиев
    scores = []  # этот массив будем сортировать

    # заполняем словари и стэки
    for line in range(0, lines):
        player = input().split()
        # Кондратии не нуждаются в сортировке, их в отдельный стэк
        if is_kondratiy(player[0]):
            kondratiy_stack.append(player)
        else:
            # для поиска LIFO если имена и очки совпадают
            players_stack.append(player)
            # сумму считаем только положительную
            score = sum([int(i) for i in player[1:] if int(i) > 0])
            if score in players_sums.keys():
                players_sums[score].append(player)
            else:
                players_sums[score] = [player]
                scores.append(score)

    # выполняем пирамидальную сортировку
    heap_sort(scores)
    n = len(scores)

    # Выводим сначала Кондратиев
    while kondratiy_stack:
        print(' '.join(kondratiy_stack.pop()))

    # распаковываем по отсортированному массиву имена и очки
    for i in range(n - 1, -1, -1):
        names = sorted(players_sums[scores[i]], reverse=True)

        while len(names) > 0:
            if len(names) > 1:
                # проверяем на одинаковые имена
                if names[-1][0] == names[-2][0]:
                    # ищем в стэке с конца, метод LIFO
                    for j in range(len(players_stack) - 1, -1, -1):
                        if players_stack[j][0] == names[-1][0] and sum(
                                [int(i) for i in players_stack[j][1:] if int(i) > 0]) == scores[i]:
                            extracted_player = ' '.join(players_stack[j])
                            print(f'{extracted_player}')
                            names.pop()
                        if len(names) == 0:
                            break
                else:
                    extracted_player = ' '.join(names.pop())
                    print(f'{extracted_player}')
            else:
                extracted_player = ' '.join(names.pop())
                print(f'{extracted_player}')
