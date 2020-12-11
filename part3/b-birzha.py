n = int(input())

prices = list(map(int, input().split()))
profit = 0

for i in range(0, n - 1):
    if prices[i] < prices[i+1]:
        profit += (prices[i+1] - prices[i])

print(profit)
