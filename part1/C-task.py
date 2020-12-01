input_handle = open("input.txt", mode='r')
output_handle = open("output.txt", mode='w')
content_list = input_handle.readlines()

lenght = int(content_list[0])
list_number = content_list[1].split(' ')
first = int(''.join(list_number))
second = int(content_list[2])
list_number = [line.rstrip() for line in list_number]
# print(first)
# print(second)
# print(first + second)
answer = str(first + second)

list_answer = ''
first_enter = True
for char in answer:
    if first_enter == False:
        list_answer += ' '
    first_enter = False
    list_answer += char

print(list_answer)
output_handle.write(list_answer)