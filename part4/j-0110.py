import math

n = int(input())
k = int(input())


# def convert_string(iter, position, string='0'):
#     if iter == 1:
#         return string[-1]
#     newstring = ''
#     for i in range(0, len(string)):
#         if string[i] == '0':
#             newstring += '01'
#         else:
#             newstring += '10'
#     iter -= 1
#     print(newstring)
#     return convert_string(iter, position, newstring[:position])
#
#
# print(convert_string(n, k))

# string = '0'
#
# for i in range(0, n):
#     newstring = ''
#     for char in string:
#         if char == '0':
#             newstring += '01'
#         else:
#             newstring += '10'
#     string = newstring
#     print(string)
# print(string[k])

# 01
# 0110
# 0110 1001
# 0110 1001 1001 0110
# 0110 1001 1001 0110 1001 0110 0110 1001
# 0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001 0110 1001 1001 0110


def generate_seq(k):
    seed = '0110'
    if k > 1:
        level = math.floor(math.log(k, 2))
    else:
        level = 1
    # print(level)
    for i in range(0, level - 1):
        mirror = seed
        mirror = mirror.replace('0', 't')
        mirror = mirror.replace('1', '0')
        mirror = mirror.replace('t', '1')

        # print(f'{seed} and {mirror}')
        seed += mirror
    return seed[k]


print(generate_seq(k - 1))
