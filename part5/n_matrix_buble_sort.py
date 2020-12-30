n = int(input())

m = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(i) for i in input().split()])




def compare(a, b, untouched):
    if a > b:
        a, b = b, a
        untouched = False
    return a, b, untouched


untouched = False
while untouched is False:
    untouched = True
    for i in range(0, n - 1):
        for j in range(0, m - 1):
            matrix[i][j], matrix[i + 1][j + 1], untouched = compare(matrix[i][j], matrix[i + 1][j + 1], untouched)

for row in matrix:
    print(*row)
