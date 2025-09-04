"""
LeetCode Problem: Coin Change (#322, Medium)
=======================================
Description:
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. You may assume that you have an infinite number of each kind of coin.

Example:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1, which uses 3 coins.

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

Solution:
This solution uses a dynamic programming approach to find the minimum number of coins needed. We create a DP array where `dp[i]` represents the minimum number of coins needed to make amount i. For each amount from 1 to the target, we try each coin denomination and update `dp[i]` if a valid combination is found. This ensures O(amount * len(coins)) time complexity and O(amount) space complexity.

Author: [Your Name]
Date: September 4, 2025
"""

def coinChange(coins: list[int], amount: int) -> int:
    """
    Find the fewest number of coins needed to make the given amount.
    Args:
        coins (List[int]): Array of coin denominations
        amount (int): Target amount
    Returns:
        int: Minimum number of coins, or -1 if impossible
    """
    # Initialize DP array with amount + 1 (impossible value)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case: 0 amount requires 0 coins
    
    # Compute minimum coins for each amount from 1 to target
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return -1 if amount cannot be made
    return dp[amount] if dp[amount] != amount + 1 else -1

# Test cases
test_cases = [
    ([1,2,5], 11, 3),       # Example 1: Standard case
    ([2], 3, -1),            # Example 2: Impossible amount
    ([1], 0, 0),             # Zero amount
    ([1,2,5], 100, 20),     # Large amount
    ([3,7,405,436], 8839, 25),  # Complex case
]

def run_tests():
    """Run test cases and print results."""
    for coins, amount, expected in test_cases:
        coins_copy = coins.copy()  # Preserve original for display
        result = coinChange(coins, amount)
        print(f"Input: coins = {coins_copy}, amount = {amount}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to find the minimum number of coins from the given denominations to make a target amount, with unlimited coins available.
   - Example: For `coins = [1,2,5]` and `amount = 11`, return 3 (using 5 + 5 + 1).
   - The challenge is to compute this efficiently for amounts up to 10^4 and up to 12 coin types, returning -1 if impossible.
   - Edge cases include zero amount, impossible amounts, or single coin types.

2. Initial Thoughts:
   - A naive recursive approach could try all combinations, but this is exponential (O(2^n)), too slow for amount ≤ 10^4.
   - A greedy approach (always picking the largest coin) fails for cases like `coins = [1,5,10], amount = 15` (greedy picks 10+5, but optimal is 5+5+5).
   - Dynamic programming seemed promising, as the problem involves optimal substructure (minimum coins for amount i depends on smaller amounts).
   - I considered a DP array to store minimum coins for each amount, which avoids recomputation.

3. Dynamic Programming Approach:
   - Define `dp[i]` as the minimum number of coins needed to make amount i.
   - Initialize `dp` with `amount + 1` (impossible value) and set `dp[0] = 0` (base case).
   - For each amount i from 1 to `amount`:
     - For each coin, if `coin <= i`, update `dp[i] = min(dp[i], dp[i - coin] + 1)`.
   - Return `dp[amount]` if it’s not `amount + 1`, else return -1.
   - This approach is O(amount * len(coins)) time (nested loops) and O(amount) space (DP array).
   - Handles edge cases like zero amount (`dp[0] = 0`) and impossible amounts (`dp[amount] = amount + 1`).

4. List Operations Used:
   - Array initialization: Create `dp = [amount + 1] * (amount + 1)` and set `dp[0] = 0`.
   - Array indexing: Access `dp[i]` and `dp[i - coin]` for updates.
   - Iteration: Use nested loops `range(1, amount + 1)` and `for coin in coins`.
   - Minimum: Use `min(dp[i], dp[i - coin] + 1)` to update DP values.

5. Key Insights:
   - The DP approach efficiently builds solutions for all amounts up to the target, reusing subproblem results.
   - Using `amount + 1` as an impossible value simplifies checking for infeasible amounts.
   - This problem relates to "House Robber" (DP with sequence optimization) and "Longest Increasing Subsequence" (DP for subsequences).
   - In a project like a payment system, this could optimize coin or bill combinations for transactions.

My Understanding of Coin Change in Real Life:
============================================
The Coin Change problem has practical applications in scenarios involving resource optimization, financial systems, or decision-making under constraints. Here are some examples:

1. Financial Systems:
   - In cash register systems, this algorithm can minimize the number of coins or bills used to make change for a customer.
   - Example: Calculating the fewest coins to return for a $11 payment with denominations [1,2,5].

2. Resource Allocation:
   - In manufacturing or logistics, this can minimize the number of resources (e.g., materials, time slots) used to meet a demand.
   - Example: Allocating the fewest number of machine hours from available durations to complete a task.

3. Task Optimization:
   - In my To-Do List Manager project, if tasks have time costs and I need to meet a total time goal, this algorithm could minimize the number of tasks selected.
   - Example: Selecting the fewest tasks to achieve a total duration of 11 hours with task durations [1,2,5].

4. Learning Takeaway:
   - This problem deepened my understanding of dynamic programming for knapsack-like problems, a pattern seen in "House Robber" and "Longest Increasing Subsequence."
   - It builds on DP skills, preparing me for more complex problems like "Coin Change II" or "Knapsack Problem."
   - In real life, I see this applying to tasks like optimizing transactions, resource allocation, or minimizing steps in processes.
   - Solving this enhances my ability to design efficient algorithms for optimization under constraints.

Next Steps:
- I can optimize with a breadth-first search (BFS) approach for specific cases or explore "Coin Change II" (counting combinations).
- I can track the coins used to reconstruct the solution, not just the count.
- Committing this to my GitHub portfolio showcases my skills in dynamic programming and optimization.
- I can explore related problems like "Coin Change II," "Minimum Cost For Tickets," or "Knapsack Problem" to further practice DP techniques.
"""

if __name__ == "__main__":
    run_tests()