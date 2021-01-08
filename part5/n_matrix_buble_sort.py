n = int(input())

m = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(i) for i in input().split()])


def compare(a, b, untouched):
    if a > b:
        a, b = b, a
        untouched = False
        # print('swap')
    return a, b, untouched


def bubble_sort(shift_i, shift_j):
    if shift_i > 0:
        cycles = n - 1 - shift_i
    elif shift_j > 0:
        cycles = m - 1 - shift_j
    else:
        cycles = min(n, m) - 1 - max(shift_i, shift_j)
    # print(f' ==== Shift {max(shift_i, shift_j)}, cycles {cycles}')
    untouched = False
    while untouched is False:
        untouched = True
        for cycle in range(cycles):
            i = cycle + shift_i
            j = cycle + shift_j
            # print(f'First is {matrix[i][j]}')
            # print(f'Second is {matrix[i + 1][j + 1]}')
            try:
                matrix[i][j], matrix[i + 1][j + 1], untouched = compare(matrix[i][j], matrix[i + 1][j + 1], untouched)
            except Exception:
                pass

def sort_diagonal(shift_i, shift_j):
    if shift_i > 0:
        cycles = n - shift_i
    elif shift_j > 0:
        cycles = m - shift_j
    else:
        cycles = min(n, m) - max(shift_i, shift_j)
    diagonal = []
    for cycle in range(cycles):
        i = cycle + shift_i
        j = cycle + shift_j
        try:
            diagonal.append(matrix[i][j])
        except Exception:
            pass
    # print(diagonal)
    diagonal = sorted(diagonal)
    # print(diagonal)
    for cycle in range(cycles):
        i = cycle + shift_i
        j = cycle + shift_j
        try:
            matrix[i][j] = diagonal[cycle]
        except Exception:
            pass

#
# untouched = False
# while untouched is False:
#     untouched = True
#     for i in range(0, n - 1):
#         for j in range(0, m - 1):
#             matrix[i][j], matrix[i + 1][j + 1], untouched = compare(matrix[i][j], matrix[i + 1][j + 1], untouched)

for y in range(0, n - 1):
    sort_diagonal(y, 0)
# print('================================================')
for x in range(1, m - 1):
    sort_diagonal(0, x)

for row in matrix:
    print(*row)
