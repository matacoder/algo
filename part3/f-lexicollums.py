n = int(input())
m = int(input())

letters = 'qwertyuiopasdfghjklzxcvbnm'
letters = sorted(letters)
dict_letters = {}
for i in range(len(letters)):
    dict_letters[letters[i]] = i
# print(dict_letters)

strings = []
to_delete = 0
for _ in range(n):
    strings.append(input())

for char_index in range(0, m):
    last_index = 0
    for row in range(0, n):
        letter = strings[row][char_index]
        if dict_letters[letter] < last_index:
            to_delete += 1
            break
        last_index = dict_letters[letter]


print(to_delete)