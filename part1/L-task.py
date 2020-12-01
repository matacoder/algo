input_handle = open("input.txt", mode='r')
output_handle = open("output.txt", mode='w')
content_list = input_handle.readlines()

content_list = [line.rstrip() for line in content_list]
# print(content_list)


line1 = sorted(content_list[0])
line2 = sorted(content_list[1])
if len(line1) < len(line2):
    line1, line2 = line2, line1
# print(line1)
result = ''
for char in range(0, len(line1)-1):
    # print('=======')
    # print(line1[char])
    # print(line2[char])
    if char == (len(line1)-2):
        if line1[char] == line2[char]:
            result = line1[char+1]
            break
    if line1[char] != line2[char]:
        result = line1[char]
        break

print(result)