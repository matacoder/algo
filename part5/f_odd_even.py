n = int(input())
if n > 0:
    numbers = input().split()
    stack = [int(i) for i in numbers]
    even = []
    odd = []

    while len(stack):
        item = stack.pop()
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    output = []
    while len(even):
        output.append(even.pop())
        output.append(odd.pop())
    print(*output)


