person, last = list(map(int, input().split()))


def get_fibonacci_last_digit(n, step):
    first = 1
    second = 1

    res = 0

    for i in range(2, n + 1):
        res = (first + second) % 10 ** step
        first = second
        second = res

    return res


print(get_fibonacci_last_digit(person, last))
