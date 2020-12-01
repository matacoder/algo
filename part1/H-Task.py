input_handle = open("input.txt", mode='r', encoding='utf-8', errors='ignore')
output_handle = open("output.txt", mode='w')
content_list = input_handle.readlines()

testline='qwertyuiopasdfghjklzxcvbnm'
check_line=[char.lower() for char in content_list[0] if char.lower() in testline]
# print(check_line)

outcome = 'True'

for i in range(0, int(len(check_line)/2)):
    if check_line[i] != check_line[-i-1]:
        outcome = 'False'
        break

output_handle.write(outcome)