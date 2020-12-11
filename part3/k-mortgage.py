number, budget = list(map(int, input().split()))
houses = sorted(list(map(int, input().split())))

# print(houses)

can_buy = 0

for house in houses:
    if budget - house >= 0:
        can_buy +=1
        budget -= house
    else:
        break
print(can_buy)
