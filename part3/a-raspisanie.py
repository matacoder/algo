def to_dotstring(item):
    item = list(str(item))
    while True:
        if item[-1] == '.':
            item.pop()
            return ''.join(item)
        elif item[-1] == '0':
            item.pop()
        else:
            return ''.join(item)


lessons = []
for _ in range(0, int(input())):
    user_input = input().split()
    # user_input = list(map(lambda s: s.replace('.', ','), user_input))
    user_input = map(float, user_input)
    lessons.append(list(user_input))

lessons = sorted(lessons)
lessons_end = sorted(lessons, key=lambda x: x[1])
# print(lessons_end)

output = [lessons_end[0]]
for i in range(1, len(lessons_end)):
    if lessons_end[i][0] >= output[-1][1]:
        output.append(lessons_end[i])

print(len(output))
for lesson in output:
    print(' '.join(list(map(to_dotstring, lesson))))

