n = input()
line = input().split(' ')
# line = [int(item) for item in line]
line = [[abs(int(i)), int(int(i)/abs(int(i)))] for i in line]

line = sorted(line, reverse=True)
line = line[:200]
line = [x * y for x, y in line]
from itertools import combinations

comb = combinations(line, 3)


output = -1

for combination in comb:
    # print(combination)
    if sum(combination) == 0:
        prod = combination[0]*combination[1]*combination[2]
        if prod > output:
            output = prod
print(output)
# line = [[abs(int(i)), int(int(i)/abs(int(i)))] for i in line]
#
# line = sorted(line, reverse=True)
# line = line[:200]
# # print(line)
#
# output = -1
#
# for i in range(0, len(line)):
#     for j in range(i+1, len(line)):
#         for k in range(j+1, len(line)):
#             # print(f'{i} * {j} * {k}')
#             if i != j and j != k and i != k:
#                 mult = line[i][1] * line[j][1] * line[k][1]
#
#                 if mult > 0:
#                     # print(mult)
#                     sum = line[i][1]*line[i][0] + line[j][1]*line[j][0] + line[k][1]*line[k][0]
#                     # print(sum)
#                     if sum == 0:
#
#                         final = line[i][0] * line[j][0] * line[k][0]
#
#                         if output < final:
#                             # print(f'{i} * {j} * {k}')
#                             # print(f'{line[i][0]} * {line[j][0]} * {line[k][0]}')
#                             # print(f'{line[i][1]} * {line[j][1]} * {line[k][1]}')
#                             # print(final)
#
#                             output = final


