n = int(input())
if n > 0:
    colors = input().split()

    stack_0 = []
    stack_1 = []
    stack_2 = []

    while len(colors):
        item = int(colors.pop())
        if item == 0:
            stack_0.append(item)
        elif item == 1:
            stack_1.append(item)
        elif item == 2:
            stack_2.append(item)

    output = stack_0 + stack_1 + stack_2
    print(*output)
