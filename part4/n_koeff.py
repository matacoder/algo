n = int(input())
m = int(input())

# n, m = max([n, m]), min([n, m])




# return (g, x, y) a*x + b*y = gcd(x, y)
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x




bezout = egcd(n, m)

bezout = list(bezout)

nod = bezout[0]

ab = bezout[1:3]

print(f'{ab[0]} {ab[1]} {nod}')
