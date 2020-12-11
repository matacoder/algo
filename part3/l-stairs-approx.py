num_of_stairs = int(input())
stairs_jumps = list(map(int, input().split()))

power_number = 1
for i in range(0, len(stairs_jumps)):
    # print(f'index: {i}, pwr-nmb: {power_number}')
    power_number -= 1
    if i == len(stairs_jumps) - 1:
        print(True)
        break
    if stairs_jumps[i] > power_number:
        # print(f'{stairs_jumps[i]} > {power_number}')
        power_number = stairs_jumps[i]

    if power_number <= 0:
        print(False)
        break
