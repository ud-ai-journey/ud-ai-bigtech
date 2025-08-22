"""
LeetCode Problem: Sort Colors (#75, Medium)
=======================================
Description:
Given an array `nums` with n objects colored red, white, or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white, and blue. We use the integers 0, 1, and 2 to represent the colors
red, white, and blue, respectively. The sorting must be done in-place without using the library's sort function.

Example:
Input: nums = [2,0,2,1,1,0]
Output: nums = [0,0,1,1,2,2]
Explanation: The array is sorted so all 0s come first, followed by all 1s, then all 2s.

Constraints:
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2

Solution:
This solution uses a three-pointer technique (Dutch National Flag algorithm) to sort the array in-place in one pass.
We maintain three pointers: `low` for the next position to place a 0, `mid` for scanning the array, and `high` for the
next position to place a 2. Elements between `low` and `mid` are 1s, before `low` are 0s, and after `high` are 2s.
This approach ensures O(n) time complexity and O(1) space complexity.

Author: [Your Name]
Date: August 22, 2025
"""

def sortColors(nums: list[int]) -> None:
    """
    Sort the array in-place so that all 0s come first, followed by 1s, then 2s.
    Args:
        nums (List[int]): Array of integers (0, 1, or 2)
    """
    low = 0              # Next position for 0
    mid = 0              # Current element being processed
    high = len(nums) - 1 # Next position for 2
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Test cases
test_cases = [
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),  # Example 1: Mixed colors
    ([2, 0, 1], [0, 1, 2]),                     # Small array
    ([1], [1]),                                  # Single element
    ([0, 0, 0], [0, 0, 0]),                     # All 0s
    ([2, 2, 1, 1, 0, 0], [0, 0, 1, अध्यक्ष1, 2, 2]), # Balanced colors
]

def run_tests():
    """Run test cases and print results."""
    for nums, expected in test_cases:
        nums_copy = nums.copy()  # Preserve original for display
        sortColors(nums)
        print(f"Input: nums = {nums_copy}")
        print(f"Output: nums = {nums}")
        print(f"Expected: nums = {expected}")
        print(f"Pass: {nums == expected}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to sort an array `nums` containing only 0s, 1s, and 2s in-place, so that all 0s come first, followed by 1s, then 2s.
   - Example: For nums=[2,0,2,1,1,0], modify to [0,0,1,1,2,2].
   - The challenge is achieving this in-place with O(1) space and in one pass for efficiency, without using a sorting library.

2. Initial Thoughts:
   - A naive approach could use a counting sort (count 0s, 1s, and 2s, then rewrite the array), but this requires two passes and O(1) extra space for counts.
   - Sorting the array with a library function (e.g., Timsort) would be O(n log n) and not allowed by the problem.
   - I considered moving all 0s to the front (like "Move Zeroes") and then sorting 1s and 2s, but this requires multiple passes.
   - I realized the Dutch National Flag algorithm, using three pointers, could sort the array in one pass by partitioning it into regions for 0s, 1s, and 2s.

3. Three-Pointer Approach (Dutch National Flag):
   - I used three pointers: `low` (next position for a 0), `mid` (current element being processed), and `high` (next position for a 2).
   - The array is partitioned so that:
     - Elements before `low` are 0s.
     - Elements between `low` and `mid` are 1s.
     - Elements after `high` are 2s.
   - While `mid <= high`:
     - If `nums[mid] == 0`, swap with `nums[low]`, increment both `low` and `mid`.
     - If `nums[mid] == 1`, increment `mid` (1 is in the correct region).
     - If `nums[mid] == 2`, swap with `nums[high]`, decrement `high` (don’t increment `mid` as the swapped element needs checking).
   - This approach is O(n) time (one pass) and O(1) space (in-place).

4. List Operations Used:
   - Indexing: Access `nums[low]`, `nums[mid]`, and `nums[high]`.
   - In-place modification: Swap elements using `nums[low], nums[mid] = nums[mid], nums[low]` or similar for `high`.
   - Iteration: Loop while `mid <= high`.
   - Length checks: Use `len(nums)` to initialize `high`.

5. Key Insights:
   - The three-pointer technique efficiently partitions the array into three regions, extending the two-pointer methods from "Move Zeroes" and "Merge Sorted Array."
   - Not incrementing `mid` after swapping with `high` is critical, as the swapped element could be 0 or 1 and needs reprocessing.
   - This problem is related to "Move Zeroes" (partitioning by zero/non-zero) and "Rotate Array" (in-place manipulation), but it handles three categories instead of two.
   - It connects to my To-Do List Manager project, where I might sort tasks by priority levels (e.g., 0=low, 1=medium, 2=high) in-place.

My Understanding of Sort Colors in Real Life:
============================================
The Sort Colors problem has practical applications in scenarios where we need to categorize and sort data into a fixed number of groups in-place, especially in memory-constrained environments. Here are some examples:

1. Data Categorization:
   - In data processing, such as sorting sensor readings into categories (e.g., low, medium, high), this algorithm can organize them in-place.
   - Example: Sorting error codes in a log file into critical (2), warning (1), and normal (0) for efficient analysis.

2. Task Prioritization:
   - In my To-Do List Manager project, if tasks are tagged with priority levels (0=low, 1=medium, 2=high), this algorithm can sort them in-place to group tasks by priority.
   - This helps display tasks in order of importance without extra storage.

3. Resource Allocation:
   - In systems like process scheduling, tasks or jobs might be categorized into three priority levels. This algorithm can reorder them in-place to ensure high-priority tasks are processed first.

4. Learning Takeaway:
   - This problem deepened my understanding of in-place partitioning and three-pointer techniques, building on two-pointer methods from "Merge Sorted Array," "Move Zeroes," and "Rotate Array."
   - It prepares me for more complex problems like "Partition Array" or "Wiggle Sort," which involve partitioning or reordering arrays.
   - In real life, I see this applying to scenarios like sorting inventory by category, prioritizing notifications, or organizing ranked search results.
   - Solving this enhances my ability to design efficient, memory-conscious algorithms for multi-category sorting.

Next Steps:
- I can enhance this by counting the number of swaps performed for performance analysis.
- I can try a variation, like sorting with more than three categories (requires a different approach, e.g., counting sort).
- Committing this to my GitHub portfolio showcases my progress in array manipulation and algorithmic problem-solving.
- I can explore related problems like "Remove Duplicates from Sorted Array II" or "Partition Array" to further practice partitioning techniques.
"""

if __name__ == "__main__":
    run_tests()