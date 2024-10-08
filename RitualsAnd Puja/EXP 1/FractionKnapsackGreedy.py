def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    # Calculate value per unit weight
    value_per_weight = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    # Sort items based on value per unit weight
    value_per_weight.sort(reverse=True)
    total_value = 0
    remaining_capacity = capacity
    for i in range(n):
        if value_per_weight[i][1] <= remaining_capacity:
            total_value += value_per_weight[i][2]
            remaining_capacity -= value_per_weight[i][1]
        else:
            total_value += value_per_weight[i][0] * remaining_capacity
            break
    return total_value

def main():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value = fractional_knapsack(weights, values, capacity)
    print("Maximum value obtained:", max_value)

if __name__ == "__main__":
    main()
