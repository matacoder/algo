# from itertools import permutations

line = input()
template = input()
lngt = len(template)
output = 0

sorted_template = sorted(template)
# per_template = permutations(template, len(template))
# per_template = [''.join(mutat) for mutat in template]

for i in range(0, len(line)-lngt+1):
    test_string = line[i:i+lngt]
    # print('test list')
    # print(test_string)
    if sorted(test_string) == sorted_template:
        output += 1

print(output)