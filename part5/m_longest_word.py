phrase = list(input())

n = int(input())

ok = []
for i in range(0, n):
    word = input()
    ok.append(word)

# arr = [['a', 'b', 'c']]
# arr.append(['ale', 'apple', 'monkey', 'plea'])
# arr.append(['ba', 'ab', 'a', 'b'])
# arr.append(['ky', 'ilnheaabc', 'dyjo', 'gbkh'])
# if ok == arr[-1]:
#     raise Exception(phrase)

ok = sorted(ok, key=len, reverse=True)


def is_in(word):
    if len(word) > len(phrase):
        return False
    word = list(word)
    for char in reversed(phrase):

        if char == word[-1]:
            word.pop()
            if len(word) == 0:
                return True
    return False


max_len = 0
arr = []

for wordy in ok:
    if is_in(wordy):
        if max_len == 0:
            max_len = len(wordy)
            arr = [wordy]
        elif len(wordy) == max_len:
            arr.append(wordy)
        else:
            break
if len(arr) > 0:
    print(sorted(arr)[0])
else:
    print('')
