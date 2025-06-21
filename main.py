import time


def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result


def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


amount = 113

start = time.time()
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start

start = time.time()
dp_result = find_min_coins(amount)
dp_time = time.time() - start

print("Greedy result:", greedy_result)
print("Greedy time: {:.6f} seconds".format(greedy_time))

print("\nDP result:", dp_result)
print("DP time: {:.6f} seconds".format(dp_time))
