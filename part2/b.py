n = int(input())
m = int(input())

matrix = []
transpond = []
for row in range (0, n):
    matrix.append(input().split(' '))


for i in range(0, m):
    list = []
    for j in range(0, n):
        list.append(matrix[j][i])
    transpond.append(list)

for row in transpond:
    print(' '.join(row))