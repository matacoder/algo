line = input()
print(line)
dic = {}

for char in line:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1
freq_az = [v[0] for v in sorted(dic.items(), key=lambda kv: (-kv[1], kv[0]))]
output = ''
for char in freq_az:
    for repeat in range(0, dic[char]):
        output += char

print(output)