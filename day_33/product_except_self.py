"""
LeetCode Problem: Product of Array Except Self (#238, Medium)
=======================================
Description:
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The solution must run in O(n) time and cannot use the division operation. The output array is the only extra space allowed (O(1) space excluding the output).

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: 
- answer[0] = 2 * 3 * 4 = 24
- answer[1] = 1 * 3 * 4 = 12
- answer[2] = 1 * 2 * 4 = 8
- answer[3] = 1 * 2 * 3 = 6

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Solution:
This solution uses a two-pass approach to compute the product of all elements except self in O(n) time and O(1) space (excluding the output array). In the first pass, we compute the product of all elements to the left of each index and store it in the output array. In the second pass, we multiply each output element by the product of all elements to the right of the index, using a running product variable. This avoids division and extra space while meeting the constraints.

Author: [Your Name]
Date: August 27, 2025
"""

def productExceptSelf(nums: list[int]) -> list[int]:
    """
    Compute the product of all elements except self for each index.
    Args:
        nums (List[int]): Array of integers
    Returns:
        List[int]: Array where each element is the product of all other elements
    """
    n = len(nums)
    answer = [1] * n  # Initialize output array with 1s
    
    # First pass: Compute products of all elements to the left of each index
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]
    
    # Second pass: Multiply by products of all elements to the right of each index
    right_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]
    
    return answer

# Test cases
test_cases = [
    ([1,2,3,4], [24,12,8,6]),        # Example 1: Sequential numbers
    ([2,3,4,5], [60,40,30,24]),      # Different numbers
    ([1,1], [1,1]),                   # All ones
    ([0,1,2,3], [6,0,0,0]),          # Array with zero
    ([-1,-2,-3,-4], [-24,-12,-8,-6]) # Negative numbers
]

def run_tests():
    """Run test cases and print results."""
    for nums, expected in test_cases:
        nums_copy = nums.copy()  # Preserve original for display
        result = productExceptSelf(nums)
        print(f"Input: nums = {nums_copy}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to return an array where each element `answer[i]` is the product of all elements in `nums` except `nums[i]`.
   - Example: For `nums = [1,2,3,4]`, return `[24,12,8,6]`, where `answer[0] = 2*3*4 = 24`, etc.
   - The challenge is to achieve O(n) time complexity without using division and with O(1) space complexity (excluding the output array).
   - The constraints ensure the input has at least 2 elements, and products fit within a 32-bit integer.

2. Initial Thoughts:
   - A naive approach could compute the total product and divide by `nums[i]` for each `answer[i]`, but division is not allowed, and zeros in the array would complicate it.
   - I considered computing left and right products for each index using extra arrays, but this requires O(n) space, violating the space constraint.
   - I realized that the output array itself could be used to store intermediate results, and a two-pass approach could combine left and right products.
   - Another idea was to handle zeros separately, but the two-pass approach works generally without special cases.

3. Two-Pass Approach:
   - I used the output array to store the product of all elements to the left of each index in the first pass.
   - In the second pass, I multiply each element by the product of all elements to the right, using a running product variable.
   - Steps:
     - Initialize `answer` with 1s (O(n)).
     - First pass: For each `i`, set `answer[i]` to the product of all elements before `i` (left_product).
     - Second pass: Iterate backward, multiplying `answer[i]` by the product of all elements after `i` (right_product).
   - This approach is O(n) time (two passes over the array) and O(1) space (only uses the output array and a few variables).
   - It avoids division and handles all cases, including zeros and negative numbers, as the product is computed directly.

4. List Operations Used:
   - Array initialization: Create `answer = [1] * n` for the output array.
   - Iteration: Loop forward (`range(n)`) for left products and backward (`range(n-1, -1, -1)`) for right products.
   - In-place modification: Update `answer[i]` with left and right products.
   - Multiplication: Use `left_product *= nums[i]` and `right_product *= nums[i]` to compute running products.

5. Key Insights:
   - Using the output array as temporary storage eliminates the need for extra space, meeting the O(1) space requirement.
   - The two-pass approach elegantly combines left and right products without division, handling all edge cases (zeros, negatives).
   - This problem relates to other array manipulation problems like "Sort Colors" or "Kth Largest Element," but focuses on prefix/suffix products.
   - In a project like a financial calculator, this could compute products of rates or values excluding specific entries for analysis.

My Understanding of Product of Array Except Self in Real Life:
============================================
The Product of Array Except Self problem has practical applications in scenarios requiring computations over arrays while excluding specific elements, especially in data processing or algorithmic systems. Here are some examples:

1. Data Analysis:
   - In statistical or financial applications, this algorithm can compute the product of all values except the current one, useful for metrics like geometric means or weighted products.
   - Example: Calculating the product of all sales figures except the current store’s sales for comparative analysis.

2. Signal Processing:
   - In signal processing, this can compute the product of all filter coefficients except the current one for certain algorithms.
   - Example: Processing audio signals where each sample’s effect is computed excluding itself.

3. Task Prioritization:
   - In my To-Do List Manager project, if tasks have numerical weights (e.g., importance scores), this algorithm could compute the combined weight of all other tasks to prioritize the current one.
   - Example: Determining the relative importance of a task by excluding its own weight from the total product.

4. Learning Takeaway:
   - This problem deepened my understanding of array manipulation and prefix/suffix techniques, a pattern seen in problems like "Trapping Rain Water" or "Maximum Product Subarray."
   - It builds on array processing skills from "Sort Colors" and "Kth Largest Element," preparing me for more complex array problems.
   - In real life, I see this applying to tasks like computing aggregated metrics, optimizing calculations in constrained environments, or processing data streams.
   - Solving this enhances my ability to design space-efficient algorithms for array-based computations.

Next Steps:
- I can explore a variation, like handling arrays with multiple zeros or computing the product with division (for learning, despite the constraint).
- I can count the number of multiplications performed to analyze performance.
- Committing this to my GitHub portfolio showcases my skills in array manipulation and space-efficient algorithms.
- I can explore related problems like "Maximum Product Subarray," "Trapping Rain Water," or "Subarray Product Less Than K" to further practice array techniques.
"""

if __name__ == "__main__":
    run_tests()