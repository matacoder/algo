from random import randint


def sub_partition(array, start, end, idx_pivot):
    if not (start <= idx_pivot <= end):
        raise ValueError('idx pivot must be between start and end')

    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start]
    i = start + 1
    j = start + 1

    while j <= end:
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1

    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1


def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return array

    idx_pivot = randint(start, end)
    i = sub_partition(array, start, end, idx_pivot)
    # print array, i, idx_pivot
    quicksort(array, start, i - 1)
    quicksort(array, i + 1, end)
    return array


n = int(input())
to_sort = []
for i in range(0, n):
    to_sort.append(input().split())
# print(to_sort)


all_solved = []

db = {}
while len(to_sort):
    score = to_sort.pop()
    name = score[0]
    solved = int(score[1])
    fee = int(score[2])
    all_solved.append(solved)
    if solved not in db:
        db[solved] = {}
    if fee not in db[solved]:
        db[solved][fee] = []
        db[solved][fee].append(name)
    else:
        db[solved][fee].append(name)
# print(db)

all_solved = list(set(all_solved))
all_solved = list(reversed(quicksort([int(i) for i in all_solved])))



for solved_item in all_solved:
    # print(solved_item)
    current_fees = list(db[solved_item].keys())
    # print(current_fees)
    current_fees = quicksort(current_fees)

    for current_fee in current_fees:
        # print(current_fee)
        current_names = db[solved_item][current_fee]
        # print(current_names)
        current_names = quicksort(current_names)
        for name_item in current_names:
            print(name_item)
