"""
LeetCode Problem: Two Sum (#1, Easy)
=====================================
Description:
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers
such that they add up to `target`. You may assume that each input has exactly one solution, and you
cannot use the same element twice. Return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Solution:
This solution uses a hash map to achieve O(n) time complexity. We iterate through the list once,
storing each number and its index in a dictionary. For each number, we check if its complement
(target - num) exists in the hash map. If it does, we return the indices. Otherwise, we add the
current number and index to the hash map.

A brute-force alternative (O(n^2)) is also provided for comparison, using nested loops to check all pairs.

Author: Boya Uday Kumar
Date: August 16, 2025
"""

def twoSum(nums, target):
    """
    Solve Two Sum using a hash map.
    Args:
        nums (List[int]): List of integers
        target (int): Target sum
    Returns:
        List[int]: Indices of two numbers that sum to target
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def twoSum_brute(nums, target):
    """
    Solve Two Sum using brute-force (for learning purposes).
    Args:
        nums (List[int]): List of integers
        target (int): Target sum
    Returns:
        List[int]: Indices of two numbers that sum to target
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Test cases
test_cases = [
    ([2, 7, 11, 15], 9),  # Example 1: [0,1]
    ([3, 2, 4], 6),       # Example 2: [1,2]
    ([3, 3], 6),           # Example 3: [0,1]
    ([1, 2, 3, 4], 8)     # Custom case: []
]

def run_tests():
    """Run test cases for both solutions and print results."""
    print("Testing twoSum (Hash Map):")
    for nums, target in test_cases:
        result = twoSum(nums, target)
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output: {result}\n")
    
    print("Testing twoSum_brute (Brute Force):")
    for nums, target in test_cases:
        result = twoSum_brute(nums, target)
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output: {result}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to find two numbers in a list that add up to a target and return their indices.
   - The problem guarantees exactly one solution, and I can't use the same element twice.
   - Example: For nums = [2,7,11,15] and target = 9, I need to find indices [0,1] because 2 + 7 = 9.

2. Initial Approach (Brute Force):
   - I first considered checking every pair of numbers using nested loops.
   - For each number at index i, I check all numbers at index j (where j > i) to see if nums[i] + nums[j] equals the target.
   - If found, return [i, j].
   - This works but is slow (O(n^2)) because it checks every possible pair.
   - Code: The `twoSum_brute` function implements this by iterating through all pairs and returning the first match.

3. Optimized Approach (Hash Map):
   - To improve efficiency, I used a hash map to store numbers and their indices.
   - For each number nums[i], I calculate the complement (target - nums[i]).
   - If the complement exists in the hash map, I found a pair, so I return [complement's index, i].
   - Otherwise, I add nums[i] and its index i to the hash map.
   - This runs in O(n) because each number is processed once, and hash map lookups are O(1) on average.
   - Code: The `twoSum` function uses a dictionary `seen` to track numbers and indices.

4. List Operations Used:
   - Iteration: Used `enumerate` to get both index and value while looping through nums.
   - List Creation: Returned a list of indices [seen[complement], i].
   - The brute-force version uses list indexing (nums[i], nums[j]) extensively.

5. Key Insights:
   - The hash map reduces time complexity by trading space for speed.
   - I had to ensure I didn't use the same element twice, which the hash map naturally handles by checking the complement before adding the current number.
   - Sorting wasn't needed here, unlike the 3Sum problem, which makes this a good starting point for list-based problems.

My Understanding of Two Sum in Real Life:
=======================================
The Two Sum problem has practical applications in many real-world scenarios where we need to find pairs that meet a specific condition. Here are a few examples:

1. Financial Transactions:
   - Imagine I'm balancing a budget and need to find two expenses that add up to a specific amount (e.g., $100).
   - Each expense is like a number in the list, and I want the indices (transaction IDs) to audit them.
   - The hash map approach is like checking a ledger: as I process each expense, I look for a previous expense that completes the sum.

2. Scheduling and Resource Allocation:
   - Suppose I'm scheduling tasks that require two resources (e.g., two team members) whose combined hours equal a target workload.
   - The indices represent the resource IDs, and the numbers are their available hours.
   - This problem helps me quickly pair resources efficiently.

3. E-commerce and Inventory:
   - In an online store, I might need to find two products whose prices sum to a gift card value.
   - The indices could represent product IDs, helping me recommend pairs to customers.
   - The hash map method ensures I can process large inventories quickly.

4. Learning Takeaway:
   - Solving Two Sum taught me how to optimize list operations using auxiliary data structures (hash map).
   - It relates to my To-Do List Manager project, where I used lists to store tasks and indices to manipulate them.
   - In real life, I see this as a way to efficiently match pairs in any system (e.g., pairing students for projects based on complementary skills).
   - This problem builds my confidence in handling list-based algorithms, preparing me for more complex problems like 3Sum.

Next Steps:
- I can enhance this by counting iterations in the brute-force version to understand its inefficiency.
- I can try variations, like finding pairs that sum to a range of values.
- Committing this to my GitHub portfolio shows my progress in algorithmic thinking and list manipulation.
"""

if __name__ == "__main__":
    run_tests()