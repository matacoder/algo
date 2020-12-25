seed = input()

az = sorted('qwertyuiopasdfghjklzxcvbnm')

string = ''
for letter in az:
    string += letter
    if letter == seed:
        break
    else:
        string += ' '

print(string)
