input_handle = open("input.txt", mode='r')
output_handle = open("output.txt", mode='w')
content_list = input_handle.readlines()

number = int(content_list[0])
number = f'{number:b}'
count = 0
for item in number:
    if item == '1':
        count += 1

output_handle.write(f'{count}')