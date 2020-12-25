# import itertools

DICT = {'(': ')'}

brackets_count = int(input())


# brackets_count -= 1
#
# brackets = ''
#
# for i in range(0, brackets_count):
#     brackets += '()'
#
# perm = list(itertools.permutations(brackets, brackets_count * 2))
#
# perm = set(perm)
# print(perm)
#
def check(string, limit):
    # print(string)
    if string[-1] == '(':
        return False
    stack = []
    # print(limit)
    test = 0
    for item in string:
        if item == '(' and test < limit:
            test += 1
            stack.append(DICT[item])
        else:
            if len(stack) > 0:
                if item != stack.pop():
                    return False
            else:
                return False
    return True


#
#
# checked = []
#
# for item in perm:
#     test_string = '(' + ''.join(item) + ')'
#     if check(test_string):
#         checked.append(test_string)
#
#
#
# for comb in sorted(checked):
#     print(comb)
to_sort = []


def gen_binary(n, prefix=''):
    if n == 0:
        if check(prefix, brackets_count):
            to_sort.append(prefix)
            # print(prefix)
    else:
        gen_binary(n - 1, prefix + '(')
        gen_binary(n - 1, prefix + ')')


gen_binary(brackets_count * 2)
for elem in sorted(to_sort):
    print(elem)
