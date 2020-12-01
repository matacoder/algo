input_handle = open("input.txt", mode='r')
output_handle = open("output.txt", mode='w')
content_list = input_handle.readlines()

number = int(content_list[0])

output_handle.write(f'{number:b}')