coins = [200, 100, 50, 20, 10, 5, 2, 1]

def FindCombinations(n, p = 0):
    if n == 0:
        return 1
    total = 0
    for coin in coins[p:]:
        if coin<=n:
            total += FindCombinations(n-coin, coins.index(coin))
    return total

print(FindCombinations(200))