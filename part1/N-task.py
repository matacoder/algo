num = int(input())

hash_table = [0]
hash = 0
while hash_table[-1] < 10000:
    hash_table.append(4 ** hash)
    hash += 1
    # print(hash_table[-1])

if num in hash_table:
    print(True)
else:
    print(False)