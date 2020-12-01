input_handle = open("input.txt", mode='r')
output_handle = open("output.txt", mode='w')
content_list = input_handle.readlines()

lenght = int(content_list[0])
list_number = content_list[1].split(' ')
list_number = [line.rstrip() for line in list_number]

list_number = [y for y in list_number if int(y) != 0]
# print(list_number)

list_answer = ''
first_enter = True
for char in list_number:
    if first_enter == False:
        list_answer += ' '
    first_enter = False
    list_answer += char
# print(list_answer)
output_handle.write(list_answer)