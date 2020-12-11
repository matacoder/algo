sub = input()
string = input()


def subs(sub, string):
    j = 0
    for i in range(0, len(string)):
        if sub[j] == string[i]:
            # print(f'Found {sub[j]}')
            j += 1
            if j == len(sub):
                return True
    return False


if len(sub) > len(string):
    print(False)
elif len(sub) == 0:
    print(True)
elif sub == string:
    print(True)
else:
    print(subs(sub, string))
