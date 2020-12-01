n = int(input())
inputs = []

def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


for read in range(0, n):
    inputs.append(input())


classes = unique(inputs)

for item in classes:
    print(item)