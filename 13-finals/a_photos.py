"""
Cпринт 13, Задача А, ревью 2
Матаков Денис
dmatakov@yandex.ru

Хранить все изображения в разных датацентрах в двух экземплярах.

15 дек 2020, 12:59:53
45502058
OK
1.272s
4.17Mb
"""


def fill_servers(capacity):
    pics = 0
    while len(capacity) >= 2:
        capacity = sorted(capacity)
        if capacity[-1] > 0 and capacity[0] > 0:
            capacity[-1] -= 1
            capacity[0] -= 1
            pics += 1

        if capacity[-1] == 0:
            capacity.pop()

        if capacity[0] == 0:
            capacity.pop(0)
    return pics


if __name__ == "__main__":
    _ = input()
    servers = sorted([int(i) for i in input().split()])
    print(fill_servers(servers))
