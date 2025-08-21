"""
LeetCode Problem: Rotate Array (#189, Medium)
=======================================
Description:
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.
The rotation must be done in-place, and the relative order of elements should be maintained after rotation.

Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: nums = [5,6,7,1,2,3,4]
Explanation: Rotating the array to the right by 3 steps moves the last 3 elements to the front.

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5

Solution:
This solution uses an in-place approach by first normalizing `k` to handle cases where `k` is larger than the array length.
We then reverse the entire array, followed by reversing the first `k` elements and the remaining `n-k` elements.
This three-step reverse approach ensures the array is rotated to the right by `k` steps with O(1) space complexity
and O(n) time complexity.

Author: [Your Name]
Date: August 21, 2025
"""

def rotate(nums: list[int], k: int) -> None:
    """
    Rotate the array to the right by k steps in-place.
    Args:
        nums (List[int]): Array of integers
        k (int): Number of steps to rotate right
    """
    # Normalize k to avoid unnecessary rotations
    n = len(nums)
    k = k % n  # If k >= n, take modulo to get effective rotations
    
    # Helper function to reverse a portion of the array
    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Step 1: Reverse the entire array
    reverse(0, n - 1)
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    # Step 3: Reverse the remaining n-k elements
    reverse(k, n - 1)

# Test cases
test_cases = [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),  # Example 1: Rotate by 3
    ([1, 2, 3, 4], 2, [3, 4, 1, 2]),                       # Rotate by 2
    ([1], 1, [1]),                                          # Single element
    ([1, 2], 3, [2, 1]),                                    # k > n
    ([1, 2, 3], 0, [1, 2, 3]),                             # No rotation
]

def run_tests():
    """Run test cases and print results."""
    for nums, k, expected in test_cases:
        nums_copy = nums.copy()  # Preserve original for display
        rotate(nums, k)
        print(f"Input: nums = {nums_copy}, k = {k}")
        print(f"Output: nums = {nums}")
        print(f"Expected: nums = {expected}")
        print(f"Pass: {nums == expected}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to rotate the array `nums` to the right by `k` steps in-place, preserving the relative order of elements.
   - Example: For nums=[1,2,3,4,5,6,7], k=3, modify to [5,6,7,1,2,3,4].
   - The challenge is performing the rotation in-place with O(1) space and handling cases where `k` is larger than the array length.

2. Initial Thoughts:
   - A naive approach could involve shifting each element right by one position `k` times, but that’s O(n*k) time, which is inefficient for large `k`.
   - Another approach could use an extra array to place elements in their rotated positions, but that requires O(n) space, violating the in-place requirement.
   - I considered cyclic replacements (moving each element to its final position in a cycle), but this is complex to implement correctly for all cases.
   - I realized that reversing the array in three steps (entire array, then first `k` elements, then remaining elements) achieves the rotation efficiently.

3. Reverse-Based Approach:
   - First, I normalize `k` by taking `k % n` to handle cases where `k` is larger than the array length `n`.
   - Step 1: Reverse the entire array (e.g., [1,2,3,4,5,6,7] becomes [7,6,5,4,3,2,1]).
   - Step 2: Reverse the first `k` elements (e.g., [7,6,5] becomes [5,6,7]).
   - Step 3: Reverse the remaining `n-k` elements (e.g., [4,3,2,1] becomes [1,2,3,4]).
   - This results in the rotated array [5,6,7,1,2,3,4].
   - The approach is O(n) time (three reverses, each O(n)) and O(1) space (in-place using only a few variables).

4. List Operations Used:
   - Indexing: Access `nums[start]` and `nums[end]` in the `reverse` helper function.
   - In-place modification: Swap elements using `nums[start], nums[end] = nums[end], nums[start]`.
   - Iteration: Loop in `reverse` while `start < end`, and call `reverse` three times with different ranges.
   - Length checks: Use `len(nums)` for `n` and to normalize `k`.

5. Key Insights:
   - The reverse-based approach elegantly solves the rotation problem by transforming it into three simpler reverse operations.
   - Normalizing `k` with `k % n` handles edge cases like `k > n` efficiently.
   - This problem is related to "Merge Sorted Array" and "Move Zeroes," as it involves in-place array manipulation, though it requires a different strategy (reversing instead of two-pointer placement).
   - It connects to my To-Do List Manager project, where I might rotate a list of tasks to prioritize recent ones while maintaining their order.

My Understanding of Rotate Array in Real Life:
============================================
The Rotate Array problem has practical applications in scenarios where we need to cyclically shift data while maintaining order, especially in memory-constrained environments. Here are some examples:

1. Circular Buffer Management:
   - In embedded systems or streaming applications, a circular buffer stores data in a fixed-size array. Rotating the array can shift older data out and make room for new data.
   - This algorithm allows in-place rotation, saving memory in resource-constrained devices.

2. Task Scheduling:
   - In my To-Do List Manager project, if tasks are stored in an array sorted by priority or time, rotating the list could simulate moving the most recent tasks to the front for review.
   - For example, rotating a task list by `k` positions could prioritize tasks added `k` days ago while keeping their relative order.

3. Display Rotations:
   - In UI design or graphics, rotating elements in a carousel (e.g., image slideshow) can be modeled as an array rotation.
   - Doing this in-place is efficient for real-time applications with limited memory.

4. Learning Takeaway:
   - This problem deepened my understanding of in-place array manipulation and introduced the reverse-based technique, complementing my experience with two-pointer methods in "Merge Sorted Array" and "Move Zeroes."
   - It prepares me for more complex problems like "Reverse Words in a String" or "Rotate List," which involve similar reversal or rotation concepts.
   - In real life, I see this applying to scenarios like rotating logs, shifting schedules, or reordering cyclic data structures.
   - Solving this enhances my ability to design memory-efficient algorithms for array-based problems.

Next Steps:
- I can enhance this by counting the number of swaps performed during reversals for performance analysis.
- I can try a variation, like rotating left instead of right or handling unsorted arrays.
- Committing this to my GitHub portfolio showcases my progress in array manipulation and algorithmic problem-solving.
- I can explore related problems like "Reverse Words in a String" or "Sort Colors" to further practice in-place techniques.
"""

if __name__ == "__main__":
    run_tests()