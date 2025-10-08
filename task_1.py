import time


COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    result = {}

    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins(amount):
    dp = {0: 0}  # Для суми 0 потрібно 0 монет
    parent = {}  # Запам'ятовуємо, яку монету використали

    for sum in range(1, amount + 1):
        for coin in COINS:
            diff = sum - coin
            if coin <= sum and diff in dp:
                new_count = dp[diff] + 1

                if sum not in dp or new_count < dp[sum]:
                    dp[sum] = new_count
                    parent[sum] = coin

    result = {}
    sum = amount
    while sum > 0:
        coin = parent[sum]
        result[coin] = result.get(coin, 0) + 1
        sum -= coin

    return result


if __name__ == "__main__":
    test_amounts = [113, 99, 37, 349, 500, 1000, 5000, 10000]
    print("\nПорівняння ефективності:\n")

    for amount in test_amounts:
        start_time = time.perf_counter()
        greedy_result = find_coins_greedy(amount)
        greedy_time = time.perf_counter() - start_time

        start_time = time.perf_counter()
        dp_result = find_min_coins(amount)
        dp_time = time.perf_counter() - start_time

        print(f"Сума {amount}:")
        print(f"Жадібний: {greedy_result}, час: {greedy_time * 1000000:.2f} мкс")
        print(f"ДП: {dp_result}, час: {dp_time * 1000000:.2f} мкс")

        ratio = dp_time / greedy_time
        if ratio > 1:
            print(f"ДП повільніше у {ratio:.1f} разів\n")
        elif ratio < 1:
            print(f"ДП швидше у {1 / ratio:.1f} разів\n")
        else:
            print("Однакова швидкість\n")
