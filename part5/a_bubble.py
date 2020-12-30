_ = input()
to_sort = [int(i) for i in input().split()]

untouched = False
iteration = 1
while untouched is False:
    untouched = True
    for position in range(0, len(to_sort) - 1):
        if to_sort[position + 1] < to_sort[position]:
            to_sort[position], to_sort[position + 1] = to_sort[position + 1], to_sort[position]
            untouched = False
    if untouched is False or iteration == 1:
        print(' '.join([str(i) for i in to_sort]))
    iteration += 1
