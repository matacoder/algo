rows = int(input())
columns = int(input())
matrix = []
for _ in range(rows):
    matrix.append(input().split())

# print(matrix)
seq = []


def is_empty(matrix):
    if len(matrix) != 0:
        if len(matrix[-1]) != 0:
            return False
    return True


def go_right(matrix, seq):
    if is_empty(matrix) is False:
        # print('Right')
        seq += matrix.pop(0)
        # print(seq)
        # print(matrix)
        return matrix, seq


def go_down(matrix, seq):
    if is_empty(matrix) is False:
        for i in range(len(matrix)):
            element = matrix[i].pop()
            # print(element)
            seq.append(element)
        # print(seq)
        return matrix, seq
    return matrix, seq


def go_left(matrix, seq):
    if is_empty(matrix) is False:
        # print('Left')
        # print(len(matrix[-1]))
        for _ in range(0, len(matrix[-1])):
            seq.append(matrix[-1].pop())
        matrix.pop()
        return matrix, seq
    return matrix, seq


def go_up(matrix, seq):
    # print(matrix)
    if is_empty(matrix) is False:
        # print('Up')
        for i in reversed(range(len(matrix))):
            seq.append(matrix[i].pop(0))
        return matrix, seq
    return matrix, seq


while is_empty(matrix) is False:
    matrix, seq = go_right(matrix, seq)
    matrix, seq = go_down(matrix, seq)
    matrix, seq = go_left(matrix, seq)
    matrix, seq = go_up(matrix, seq)

for element in seq:
    print(str(element))
