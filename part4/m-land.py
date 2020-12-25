n = int(input())
m = int(input())

n, m = max([n, m]), min([n, m])


def sq(n, m):

    if n % m == 0:
        return m
    return sq(m, n % m)


print(sq(n, m))
