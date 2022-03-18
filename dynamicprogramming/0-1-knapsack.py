"""
Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which
will give us maximum profit such that their cumulative weight is not more than a given number ‘C’.
Write a function that returns the maximum profit. Each item can only be selected once, which means either we put
an item in the knapsack or skip it.
"""
import time


def top_down_approach_knapsack(profits, weights, capacity):
    # Take it or not take it
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits))]

    def dp(pos, current_capacity):
        if current_capacity <= 0 or pos >= len(weights) or weights[pos] > current_capacity:
            return 0

        if memo[pos][current_capacity] != -1:
            return memo[pos][current_capacity]

        take_it = profits[pos] + dp(pos + 1, current_capacity - weights[pos])
        not_take_it = dp(pos + 1, current_capacity)

        memo[pos][current_capacity] = max(take_it, not_take_it)

        return memo[pos][current_capacity]

    return dp(0, capacity)


def bottom_up_approach_knapsack(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits))]

    for i in range(len(profits)):
        dp[i][0] = 0

    for idx in range(len(profits)):
        for jdx in range(1, capacity + 1):

            if idx == 0:
                if weights[idx] < capacity:
                    dp[idx][jdx] = weights[idx]
                else:
                    dp[idx][jdx] = 0
            else:
                if weights[idx] > jdx:
                    dp[idx][jdx] = dp[idx - 1][jdx]

                else:
                    dp[idx][jdx] = max(dp[idx - 1][jdx], profits[idx] + dp[idx - 1][jdx - weights[idx]])

    return dp[len(profits) - 1][capacity]


def main():
    print(bottom_up_approach_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(bottom_up_approach_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(bottom_up_approach_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
