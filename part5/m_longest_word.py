phrase = sorted(input())

n = int(input())

ok = []
for i in range(0, n):
    word = input()
    ok.append(word)

ok = sorted(ok, key=len, reverse=True)


def is_in(word):
    word = sorted(word)
    for char in word:
        if char not in phrase:
            return False
    return True


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
