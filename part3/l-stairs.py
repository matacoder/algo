'''
Входной файл
40
4 15 0 4 0 0 0 0 18 7 7 1 13 8 12 13 10 6 3 19 8 13 4 4 6 13 0 19 16 13 8 17 15 18 14 18 3 17 20 18
True
'''

num_of_stairs = int(input())
stairs_jumps = list(map(int, input().split()))
log = [0]
elevation = 0


# print(f'{stairs_jumps}')


def shift_left(elevation, jump):
    # print(f'Shift is here, eval: {elevation}, jump: {jump}')
    while jump > 1:
        elevation -= 1
        jump -= 1
        if stairs_jumps[elevation] != 0:
            # print(f'Found new hero: {stairs_jumps[elevation]}')
            return find_path(elevation)
    elevation -= 1
    stairs_jumps[elevation] = 0
    # print(f'{stairs_jumps}')
    if len(log) > 0:
        # print(f'Another try')
        return find_path(log.pop())
    else:
        return False


def find_path(elevation):
    # print('Find_path is here')
    if stairs_jumps[elevation] != 0:

        while elevation < num_of_stairs:
            jump = stairs_jumps[elevation]
            elevation += jump
            # print(f'Jump: {jump}, elev: {elevation}')
            if elevation >= num_of_stairs:
                return True
            elif elevation < num_of_stairs:
                if stairs_jumps[elevation] == 0:
                    # print(f'Fuck, zero')
                    return shift_left(elevation, jump)
            log.append(elevation)
            # print(f'Log updated: {log}')
    else:
        return False


print(find_path(elevation))

#
#
# jump = stairs_jumps[0]  # высота 1 прыжка
# count = 0
#
# elevation = 0  # позиция после 1 прыжка
# jump_history[count] = elevation
# # print(f'prev: None, next: {jump}, elev: {elevation}')
# # если первая позиция 0 - проигрыш
# if jump != 0:
#     # дальше будет либо удачный прыжок на число, либо
#     # очередной прыжок на 0, тогда нужно будет прыгать на
#     # ступеньку назад, но не более ступенек чем прыжок был изначально
#     while elevation < num_of_stairs:
#         prev_jump, jump = jump, stairs_jumps[elevation]
#
#         # print(f'prev: {prev_jump}, next: {jump}, elev: {elevation}')
#
#         # прыжок может быть на 0, тогда спускаемся
#         if jump == 0:
#
#             while prev_jump > 1:
#                 elevation -= 1
#                 prev_jump -= 1
#                 # print(f'Step back to jump {stairs_jumps[elevation]} at elev: {elevation}')
#                 # если нашли число, значит используем его
#                 if stairs_jumps[elevation] != 0:
#                     break
#         # все-таки нет тут больше чисел, только нули
#         if stairs_jumps[elevation] == 0:
#             # мы принудительно делаем наш прыжок последний нулем
#             stairs_jumps[elevation-1] = 0
#
#             break
#         # нашли число, это прыжок, значит прыгаем туда
#         jump = stairs_jumps[elevation]
#         elevation += jump
#
# if elevation >= num_of_stairs:
#     print('True')
# else:
#     print('False')
