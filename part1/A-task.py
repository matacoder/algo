input_handle = open("input.txt", mode='r')
output_handle = open("output.txt", mode='w')
content_list = input_handle.readlines()[0]

variables = content_list.split(' ')
a, x, b, c = [int(var) for var in variables]

y = a * x * x + b * x + c
# print(y)
output_handle.write(str(y))