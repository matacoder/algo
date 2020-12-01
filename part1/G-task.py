input_handle = open("input.txt", mode='r', encoding='utf-8', errors='ignore')
output_handle = open("output.txt", mode='w')
content_list = input_handle.readlines()


list_number1 = content_list[0].split(' ')
list_number1 = [line.rstrip() for line in list_number1]
list_number2 = content_list[1].split(' ')
list_number2 = [line.rstrip() for line in list_number2]


if sorted(list_number1[0]) == sorted(list_number2[0]):
    list_answer = 'True'
else:
    list_answer = 'False'
output_handle.write(list_answer)