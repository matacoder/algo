_ = input()
_ = input()
challenge1 = sorted(input().split())
challenge2 = sorted(input().split())

if len(challenge2) > len(challenge1):
    challenge1, challenge2 = challenge2, challenge1

print(challenge1)
print(challenge2)

while len(challenge1):
    if challenge1[-1] == challenge2[-1]:
        