capacity = int(input())
count = int(input())
items = []

for number in range(count):
    string = list(map(int, (input().split())))
    string.append(number)
    items.append(string)

# print(items)

items = sorted(items, key=lambda x: x[1])
# print(items)
items = sorted(items, key=lambda x: x[0], reverse=True)
# print(items)

current_weight = 0
put_into = []
for item in items:
    if current_weight + item[1] <= capacity:
        put_into.append(item)
        current_weight += item[1]

# print(put_into)
put_into = sorted([x[2] for x in put_into])
put_into = ' '.join(list(map(str, put_into)))
print(put_into)
