lenght = int(input())
scores = list(map(int, input().split()))

maximum = 1
temp = 1
for i in range(1, len(scores)):
    if scores[i-1] < scores[i]:
        temp += 1
    else:
        if temp > maximum:
            maximum = temp
        temp = 1
if temp > maximum:
    maximum = temp
print(maximum)
