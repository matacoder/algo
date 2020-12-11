kids = int(input())
factor = sorted(map(int, input().split()))

num_of_cookies = int(input())
cookies = sorted(map(int, input().split()))
# print(factor)
# print(cookies)

happy_kids = 0
cycle = 0
while True:

    cycle +=1
    # print(f' Cycle {cycle}')
    # print(factor[-1])
    # print(cookies[-1])
    if factor[-1] <= cookies[-1]:
        happy_kids += 1
        factor.pop()
        cookies.pop()
        # print(f'Kid found: {happy_kids}')
    elif factor[-1] > cookies[-1]:
        factor.pop()
    if len(cookies) == 0 or len(factor) == 0:
        break

print(happy_kids)

