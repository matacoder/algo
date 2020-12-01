input_handle = open("input.txt", mode='r', encoding='utf-8', errors='ignore')
output_handle = open("output.txt", mode='w')
content_list = input_handle.readlines()


list_number1 = content_list[1].split(' ')
list_number1 = [line.rstrip() for line in list_number1]
seen = {}
# print(list_number1)
for x in list_number1:
    if x not in seen:
        seen[x] = 1
    else:
        seen[x] += 1
output =''
# print(seen)
for talon, count in seen.items():
    if count == 1:
        output = talon
print(output)
# output_handle.write(output)