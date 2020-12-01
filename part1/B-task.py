input_handle = open("input.txt", mode='r')
output_handle = open("output.txt", mode='w')
content_list = input_handle.readlines()

universities = content_list[0].split(' ')
universities = [line.rstrip() for line in universities]
top = int(content_list[1])

visitors = {}
for visitor in universities:
    visitor = int(visitor)
    if visitor in visitors:
        current_count = int(visitors[visitor])
        visitors[visitor] = current_count + 1
    else:
        visitors[visitor] = 1

# print(visitors)
top_array = [v[0] for v in sorted(visitors.items(), key=lambda kv: (-kv[1], kv[0]))]

top_array = [str(int) for int in top_array[:top]]
# print(top_array)
output_handle.write(' '.join(top_array))