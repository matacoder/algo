def count_change(money, coins):
    if money == 0:
        return 1
    elif len(coins) == 0 or money < 0:
        return 0
    else:
        return count_change(money - coins[0], coins) + count_change(money, coins[1:])


if __name__ == "__main__":
    amount = int(input())
    _ = input()
    coins = [int(i) for i in input().split()]
    print(count_change(amount, coins))
