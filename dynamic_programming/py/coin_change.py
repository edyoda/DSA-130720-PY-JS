coins = [1,6,5]
minimum_coin_change = [0]*11

def no_of_change(money,coins):
    for m in range(1,money+1):
        minimum_coin_change[m] = float("inf")
        for coin in coins:
            if m >= coin:
                temp_min = minimum_coin_change[m-coin] + 1
                if temp_min < minimum_coin_change[m]:
                    minimum_coin_change[m] = temp_min
    return minimum_coin_change[money]

print(no_of_change(10,coins))
print(minimum_coin_change)