input_handle = open("input.txt", mode='r', encoding='utf-8', errors='ignore')
output_handle = open("output.txt", mode='w')
content_list = input_handle.readlines()

content_list = [line.rstrip() for line in content_list]

if len(content_list[0]) < len(content_list[1]):
    binary1, binary2 = content_list[1], content_list[0]
else:
    binary1, binary2 = content_list[0], content_list[1]
print(binary1)
print(binary2)
binary3 = ''
extra=0
for i in range (1, len(binary1)+1):
    print('=======')
    if extra==1:
        print('extra obtained')
    print(binary1[-i])
    if len(binary2)>=i:
        second = int(binary2[-i])
    else:
        second = 0
    print(second)
    sum_action = int(binary1[-i])+ second + extra
    if sum_action == 2:
        print('extra of 2')
        extra=1
        binary3 += '0'
    elif sum_action == 3:
        print('extra of 3')
        extra = 1
        binary3 += '1'
    elif sum_action == 1:
        print('no extra of 1')
        extra = 0
        binary3 += '1'
    elif sum_action == 0:
        print('no extra of 1')
        extra = 0
        binary3 += '0'
if extra == 1:
    binary3 += '1'

binary3 = [item for item in reversed(binary3)]


print(binary3)


output_handle.write(''.join(binary3))