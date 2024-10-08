def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a table to store the maximum value that can be achieved with
    # the first i items and a knapsack capacity of j
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # If the current item's weight is more than the current capacity,
            # then this item cannot be included in the knapsack
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            # Otherwise, consider including the current item and maximize the value
            else:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])

    # Reconstruct the selected items
    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected_items

def main():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value, selected_items = knapsack(weights, values, capacity)
    print("Maximum value:", max_value)
    print("Selected items:", selected_items)

if __name__ == "__main__":
    main()
