def knapsack_0_1(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]
    selected_items = []

    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()
    return max_value, selected_items

if __name__ == "__main__":
    values = [60, 100, 120]  # Values of items
    weights = [10, 20, 30]  # Weights of items
    capacity = 50  # Knapsack capacity

    max_value, selected_items = knapsack_0_1(values, weights, capacity)

    print("Maximum value in the knapsack:", max_value)
    print("Selected items (0-indexed):", selected_items)
