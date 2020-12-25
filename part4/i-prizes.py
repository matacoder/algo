winners = int(input())
ncoins = int(input())
coins = sorted(list(map(int, input().split())))
# print(coins)
# print(sum(coins) % winners)


def collect_coins(fund, array_coins, people):
    if len(array_coins) == 0:
        return True
    if array_coins[-1] > fund:
        return False
    if array_coins[-1] == fund:
        array_coins.pop()
        return collect_coins(fund, array_coins, people - 1)
    if array_coins[-1] < fund:
        test_fund = array_coins.pop()
        i = 0
        while test_fund < fund:
            test_fund += array_coins.pop(i)

            if test_fund == fund:
                return collect_coins(fund, array_coins, people - 1)
        if test_fund > fund:
            return False


if sum(coins) % winners == 0:
    # print('Can divide')
    fund_raise = int(sum(coins) / winners)
    print(collect_coins(fund_raise, coins, winners))
else:
    print('False')