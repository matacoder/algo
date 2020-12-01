n = int(input()) # x строки
m = int(input()) # y столбцы

matrix = []

for row in range (0, n):
    matrix.append(input().split(' '))

x = int(input())
y = int(input())

# print(matrix)

coord = []
# if 0 < x < n and 0 < y < m:
if y + 1 < m:
    coord.append(matrix[x][y + 1])

if x - 1 >= 0:
    coord.append(matrix[x - 1][y])

if x + 1 < n:
    coord.append(matrix[x + 1][y])

if y - 1 >= 0:
    coord.append(matrix[x][y - 1])

coord = [int(i) for i in coord]
coord = sorted(coord)
coord = [str(i) for i in coord]
coord = ' '.join(coord)

print(coord)