"""
LeetCode Problem: Maximum Product Subarray (#152, Medium)
=======================================
Description:
Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product. The answer is guaranteed to fit in a 32-bit integer.

Example:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: The subarray [2,3] has the largest product 6.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any prefix or subarray of nums is guaranteed to fit in a 32-bit integer.

Solution:
This solution uses a dynamic programming approach to track both the maximum and minimum products ending at each index, as negative numbers can flip the maximum to minimum and vice versa. For each element, we compute the maximum and minimum products considering the current element alone or multiplied with previous products. This ensures O(n) time complexity and O(1) space complexity, as we only store a few variables.

Author: [Your Name]
Date: September 1, 2025
"""

def maxProduct(nums: list[int]) -> int:
    """
    Find the maximum product of a contiguous subarray.
    Args:
        nums (List[int]): Array of integers
    Returns:
        int: Maximum product of a contiguous subarray
    """
    if not nums:
        return 0
    
    # Initialize max and min products ending at current index, and global max
    max_so_far = nums[0]
    curr_max = nums[0]
    curr_min = nums[0]
    
    for i in range(1, len(nums)):
        # Store curr_max for use in curr_min calculation
        temp_max = curr_max
        # Maximum product is either the current number, or the product with previous max/min
        curr_max = max(nums[i], max(nums[i] * temp_max, nums[i] * curr_min))
        # Minimum product is either the current number, or the product with previous max/min
        curr_min = min(nums[i], min(nums[i] * temp_max, nums[i] * curr_min))
        # Update global maximum
        max_so_far = max(max_so_far, curr_max)
    
    return max_so_far

# Test cases
test_cases = [
    ([2,3,-2,4], 6),         # Example 1: Mixed positive and negative
    ([-2,0,-1], 0),          # Example 2: Zeros and negatives
    ([3], 3),                 # Single element
    ([-2,-3,-4], 12),        # All negatives
    ([2,-5,-2,-4,3], 24),    # Multiple negatives
]

def run_tests():
    """Run test cases and print results."""
    for nums, expected in test_cases:
        nums_copy = nums.copy()  # Preserve original for display
        result = maxProduct(nums)
        print(f"Input: nums = {nums_copy}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to find a contiguous subarray in `nums` with the maximum product and return that product.
   - Example: For `nums = [2,3,-2,4]`, the subarray `[2,3]` gives the maximum product 6.
   - The challenge is to handle negative numbers (which can flip max/min products) and zeros (which reset products), within O(n) time and minimal space, given array size up to 2*10^4.
   - The product is guaranteed to fit in a 32-bit integer.

2. Initial Thoughts:
   - A naive approach could compute the product of every possible subarray, but this is O(n^2), too slow for n up to 2*10^4.
   - I considered a prefix product approach, but zeros and negatives complicate it, requiring resets or division.
   - I realized that negative numbers mean we need to track both maximum and minimum products at each position, as a negative number could turn a minimum product into a maximum.
   - A dynamic programming approach tracking max/min products ending at each index seemed promising, similar to Kadane’s algorithm for maximum sum subarray.

3. Dynamic Programming Approach:
   - For each index i, maintain:
     - `curr_max`: Maximum product of a subarray ending at index i.
     - `curr_min`: Minimum product of a subarray ending at index i.
     - `max_so_far`: Global maximum product seen so far.
   - For each `nums[i]`:
     - Compute new `curr_max` as the maximum of:
       - `nums[i]` (start a new subarray).
       - `nums[i] * prev_max` (extend maximum product).
       - `nums[i] * prev_min` (extend minimum product, relevant if `nums[i]` is negative).
     - Compute new `curr_min` similarly.
     - Update `max_so_far` with the new `curr_max`.
   - Initialize with `nums[0]` to handle the first element.
   - This approach is O(n) time (single pass) and O(1) space (only a few variables).

4. List Operations Used:
   - Array indexing: Access `nums[i]` for processing.
   - Variable updates: Update `curr_max`, `curr_min`, and `max_so_far` with `max()` and `min()`.
   - Iteration: Loop through `range(1, len(nums))` to process elements.
   - Temporary variable: Store `curr_max` before updating to use in `curr_min` calculation.

5. Key Insights:
   - Tracking both maximum and minimum products is crucial due to negative numbers, which can swap max/min when multiplied.
   - The approach handles zeros naturally, as they reset the product, and the single-element case is covered by initialization.
   - This problem relates to "Maximum Subarray" (Kadane’s algorithm) but adapts it for products, handling negatives and zeros.
   - In a project like a financial analyzer, this could find the maximum product of returns over a period.

My Understanding of Maximum Product Subarray in Real Life:
============================================
The Maximum Product Subarray problem has practical applications in scenarios involving sequential data and multiplicative metrics, especially in finance, signal processing, or optimization. Here are some examples:

1. Financial Analysis:
   - In stock or investment analysis, this algorithm can find the maximum product of consecutive daily returns, indicating the best period for compounded returns.
   - Example: Identifying the best week to hold a stock based on daily return factors.

2. Signal Processing:
   - In audio or signal processing, this can find the maximum product of consecutive signal amplitudes, useful for detecting peak patterns.
   - Example: Analyzing a sequence of signal gains to find the strongest continuous segment.

3. Task Optimization:
   - In my To-Do List Manager project, if tasks have multiplicative efficiency scores, this algorithm could find the sequence of tasks with the highest combined efficiency.
   - Example: Optimizing a sequence of tasks to maximize productivity over a period.

4. Learning Takeaway:
   - This problem deepened my understanding of dynamic programming for multiplicative problems, extending patterns from "Maximum Subarray."
   - It builds on array processing skills from "Product of Array Except Self" and "Kth Largest Element," preparing me for more complex DP problems.
   - In real life, I see this applying to tasks like optimizing sequential processes, analyzing time-series data, or maximizing returns in constrained windows.
   - Solving this enhances my ability to design efficient algorithms for sequential data analysis.

Next Steps:
- I can explore a variation, like finding the subarray itself or handling larger integers with modulo constraints.
- I can count the number of operations to analyze performance.
- Committing this to my GitHub portfolio showcases my skills in dynamic programming and array processing.
- I can explore related problems like "Maximum Subarray," "House Robber," or "Product of Array Except Self" to further practice DP techniques.
"""

if __name__ == "__main__":
    run_tests()