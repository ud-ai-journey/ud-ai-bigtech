"""
LeetCode Problem: Move Zeroes (#283, Easy)
=======================================
Description:
Given an integer array `nums`, move all 0's to the end of the array in-place while maintaining the relative order
of the non-zero elements. The operation must be done in-place without making a copy of the array.

Example:
Input: nums = [0,1,0,3,12]
Output: nums = [1,3,12,0,0]
Explanation: All zeroes are moved to the end, and non-zero elements keep their relative order.

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Solution:
This solution uses a two-pointer technique to move all non-zero elements to the front of the array in-place,
followed by filling the remaining positions with zeroes. We use a `non_zero_pointer` to track where the next
non-zero element should be placed and iterate through the array to place non-zero elements. Then, we fill the
rest of the array with zeroes. This approach ensures O(1) space complexity and O(n) time complexity.

Author: [Your Name]
Date: August 20, 2025
"""

def moveZeroes(nums: list[int]) -> None:
    """
    Move all zeroes to the end of the array in-place while preserving the order of non-zero elements.
    Args:
        nums (List[int]): Array of integers
    """
    # Pointer for the next position to place a non-zero element
    non_zero_pointer = 0
    
    # Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_pointer] = nums[i]
            non_zero_pointer += 1
    
    # Fill the remaining positions with zeroes
    while non_zero_pointer < len(nums):
        nums[non_zero_pointer] = 0
        non_zero_pointer += 1

# Test cases
test_cases = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),  # Example 1: Move zeroes to end
    ([1], [1]),                            # Single element: no zeroes
    ([0], [0]),                            # Single zero
    ([1, 2, 3], [1, 2, 3]),               # No zeroes
    ([0, 0, 0, 1], [1, 0, 0, 0]),         # Multiple zeroes
]

def run_tests():
    """Run test cases and print results."""
    for nums, expected in test_cases:
        nums_copy = nums.copy()  # Preserve original for display
        moveZeroes(nums)
        print(f"Input: nums = {nums_copy}")
        print(f"Output: nums = {nums}")
        print(f"Expected: nums = {expected}")
        print(f"Pass: {nums == expected}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to modify the array `nums` in-place to move all zeroes to the end while keeping the relative order
     of non-zero elements.
   - Example: For nums=[0,1,0,3,12], modify to [1,3,12,0,0].
   - The challenge is doing this in-place without using extra space, and ensuring non-zero elements maintain their order.

2. Initial Thoughts:
   - A naive approach could involve creating a new array to store non-zero elements followed by zeroes, but that uses O(n) extra space.
   - I considered counting zeroes and shifting elements, but that would require multiple passes or complex shifting.
   - Since I only need to move zeroes to the end and preserve non-zero order, I realized a two-pointer approach could
     efficiently place non-zero elements at the front and then fill the rest with zeroes.
   - This is similar to filtering elements, like in "Remove Duplicates from Sorted Array" or "Merge Sorted Array."

3. Two-Pointer Approach:
   - I used a `non_zero_pointer` to track where the next non-zero element should be placed, starting at index 0.
   - I iterate through the array with index `i`. If `nums[i]` is non-zero, I copy it to `nums[non_zero_pointer]`
     and increment `non_zero_pointer`.
   - After the loop, `non_zero_pointer` marks the position where all non-zero elements have been placed.
   - I then fill the array from `non_zero_pointer` to the end with zeroes.
   - This approach is O(n) time (two passes: one to move non-zero elements, one to fill zeroes) and O(1) space (in-place).

4. List Operations Used:
   - Indexing: Access `nums[i]` and assign to `nums[non_zero_pointer]`.
   - In-place modification: Update `nums[non_zero_pointer]` with non-zero elements and later with zeroes.
   - Iteration: Loop through the array with `i` from 0 to len(nums)-1, then from `non_zero_pointer` to len(nums)-1.
   - Length checks: Use `len(nums)` to set loop bounds.

5. Key Insights:
   - The two-pointer technique simplifies in-place manipulation by separating the placement of non-zero elements
     from the filling of zeroes.
   - This problem is similar to "Remove Duplicates from Sorted Array," where I used a pointer to place unique elements,
     and "Merge Sorted Array," where I used pointers to place sorted elements.
   - The key is to process non-zero elements first and handle zeroes last, leveraging the in-place requirement.
   - This connects to my To-Do List Manager project, where I might want to prioritize non-zero priority tasks and
     move "zero-priority" tasks to the end.

My Understanding of Move Zeroes in Real Life:
============================================
The Move Zeroes problem has practical applications in scenarios where we need to reorganize data by prioritizing
certain elements while deferring others, all while using minimal memory. Here are some examples:

1. Data Filtering:
   - In data processing, such as analyzing sensor data, I might want to move invalid readings (e.g., zeroes) to the
     end of a dataset while keeping valid readings in order.
   - This algorithm allows in-place reorganization, which is useful for large datasets in embedded systems.

2. Task Prioritization:
   - In my To-Do List Manager project, if tasks have priorities (non-zero for important, zero for optional), I could
     move zero-priority tasks to the end while preserving the order of important tasks.
   - This helps focus on high-priority tasks without needing extra storage.

3. Resource Allocation:
   - In systems like memory management, I might need to move active data (non-zero) to the front of a buffer and
     clear unused slots (zeroes) to the end, all in-place to save memory.

4. Learning Takeaway:
   - This problem strengthened my understanding of in-place array operations and two-pointer techniques, building on
     my experience with "Merge Sorted Array" and "Remove Duplicates from Sorted Array."
   - It’s a stepping stone to more complex problems like "Sort Colors" or "Partition Array," which involve similar
     in-place rearrangements.
   - In real life, I see this applying to scenarios like reorganizing a sorted playlist (moving skipped songs to the end)
     or prioritizing search results (moving irrelevant results to the end).
   - Solving this enhances my ability to write efficient, memory-conscious code for array manipulation.

Next Steps:
- I can enhance this by counting the number of zeroes moved (e.g., print len(nums) - non_zero_pointer).
- I can try a variation, like moving specific values (e.g., all 1’s) to the end instead of zeroes.
- Committing this to my GitHub portfolio showcases my progress in array manipulation and algorithmic problem-solving.
- I can explore related problems like "Remove Element" or "Sort Colors" to further practice in-place techniques.
"""

if __name__ == "__main__":
    run_tests()