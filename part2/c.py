string = str(input())


best = 0
sequence = ''
current = 0

for char in string:
    if char not in sequence:
        sequence += char
        current += 1
    else:
        tempseq = ''
        for tchar in reversed(sequence):
            if tchar != char:
                tempseq += tchar
            else:
                break
        tempseq = ''.join([char for char in reversed(tempseq)])
        sequence = tempseq + char
        if current > best:
            best = current
        current = len(sequence)
if current > best:
    best = current

print(str(best))
