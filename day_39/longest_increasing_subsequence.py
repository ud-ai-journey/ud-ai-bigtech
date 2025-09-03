"""
LeetCode Problem: Longest Increasing Subsequence (#300, Medium)
=======================================
Description:
Given an integer array `nums`, return the length of the longest strictly increasing subsequence. A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], which has length 4.

Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

Solution:
This solution uses a dynamic programming approach to find the length of the longest increasing subsequence. For each index i, we compute the length of the longest increasing subsequence ending at i by checking all previous indices j where nums[j] < nums[i]. We store these lengths in a DP array and return the maximum. To optimize space, we could use a binary search approach, but this solution prioritizes clarity with O(n^2) time complexity and O(n) space complexity.

Author: [Your Name]
Date: September 3, 2025
"""

def lengthOfLIS(nums: list[int]) -> int:
    """
    Find the length of the longest strictly increasing subsequence.
    Args:
        nums (List[int]): Array of integers
    Returns:
        int: Length of the longest increasing subsequence
    """
    if not nums:
        return 0
    
    n = len(nums)
    # dp[i] represents the length of the longest increasing subsequence ending at index i
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Test cases
test_cases = [
    ([10,9,2,5,3,7,101,18], 4),  # Example 1: Mixed values
    ([0,1,0,3,2,3], 4),          # Example 2: Repeated values
    ([7], 1),                     # Single element
    ([1,3,6,7,9,4,10,5,6], 6),   # Longer subsequence
    ([2,2,2,2], 1),              # All same elements
]

def run_tests():
    """Run test cases and print results."""
    for nums, expected in test_cases:
        nums_copy = nums.copy()  # Preserve original for display
        result = lengthOfLIS(nums)
        print(f"Input: nums = {nums_copy}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to find the length of the longest strictly increasing subsequence in `nums`, where elements must be in ascending order and can be non-contiguous.
   - Example: For `nums = [10,9,2,5,3,7,101,18]`, the subsequence `[2,3,7,101]` has length 4.
   - The challenge is to compute this efficiently for arrays up to 2500 elements, handling duplicates and negative numbers.
   - Only the length is needed, not the subsequence itself.

2. Initial Thoughts:
   - A naive approach could generate all possible subsequences and check for increasing order, but this is exponential (O(2^n)), too slow for n ≤ 2500.
   - I considered a recursive approach with memoization, but dynamic programming seemed more straightforward for subsequences.
   - A DP array `dp[i]` could represent the length of the longest increasing subsequence ending at index i, computed by checking previous elements.
   - I also noted a binary search approach could achieve O(n log n) time, but chose the O(n^2) DP solution for clarity and simplicity.

3. Dynamic Programming Approach:
   - Define `dp[i]` as the length of the longest increasing subsequence ending at index i.
   - For each index i, iterate over previous indices j (0 to i-1):
     - If `nums[j] < nums[i]`, the subsequence ending at j can be extended to include `nums[i]`, so update `dp[i] = max(dp[i], dp[j] + 1)`.
   - Initialize `dp` with 1s (each element is a subsequence of length 1).
   - Return the maximum value in `dp` as the result.
   - This approach is O(n^2) time (nested loops) and O(n) space (DP array).
   - Handles edge cases like single elements or all identical elements naturally.

4. List Operations Used:
   - Array indexing: Access `nums[i]` and `nums[j]` for comparison.
   - DP array: Initialize `dp = [1] * n` and update `dp[i]`.
   - Iteration: Use nested loops `range(n)` and `range(i)` for DP updates.
   - Maximum: Use `max(dp)` to find the final result.

5. Key Insights:
   - The DP approach efficiently builds subsequences by considering all valid previous elements, avoiding exponential complexity.
   - Tracking only the length simplifies the solution, and the O(n^2) time is acceptable for n ≤ 2500.
   - This problem relates to "House Robber" (DP with sequence constraints) and "Maximum Product Subarray" (DP with max tracking).
   - In a project like a data analyzer, this could find the longest increasing trend in a sequence of measurements.

My Understanding of Longest Increasing Subsequence in Real Life:
============================================
The Longest Increasing Subsequence problem has practical applications in scenarios involving sequence analysis, optimization, or pattern detection. Here are some examples:

1. Data Analysis:
   - In time-series data (e.g., stock prices, temperatures), this algorithm can find the longest period of strictly increasing values.
   - Example: Identifying the longest sequence of increasing stock prices for trend analysis.

2. Task Scheduling:
   - In scheduling tasks with dependencies or priorities, this can find the longest sequence of tasks with increasing priority or completion time.
   - Example: Optimizing a project timeline by selecting the longest sequence of tasks with increasing deadlines.

3. Task Optimization:
   - In my To-Do List Manager project, if tasks have numerical attributes (e.g., priority scores), this algorithm could identify the longest sequence of tasks with increasing priority.
   - Example: Planning a sequence of tasks to tackle in order of increasing urgency.

4. Learning Takeaway:
   - This problem deepened my understanding of dynamic programming for subsequence problems, a pattern seen in "House Robber" and "Maximum Product Subarray."
   - It builds on sequence optimization skills, preparing me for more complex DP problems like "Longest Common Subsequence" or "House Robber II."
   - In real life, I see this applying to tasks like analyzing trends, optimizing sequences, or detecting patterns in ordered data.
   - Solving this enhances my ability to design efficient algorithms for sequence-based optimization.

Next Steps:
- I can optimize with a binary search approach for O(n log n) time, using a patience-sorting-like method.
- I can explore a variation, like finding the subsequence itself or handling non-strictly increasing sequences.
- Committing this to my GitHub portfolio showcases my skills in dynamic programming and subsequence optimization.
- I can explore related problems like "Longest Common Subsequence," "House Robber II," or "Increasing Triplet Subsequence" to further practice DP techniques.
"""

if __name__ == "__main__":
    run_tests()