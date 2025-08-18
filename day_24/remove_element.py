"""
LeetCode Problem: Remove Element (#27, Easy)
============================================
Description:
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place.
The order of the elements may be changed. Return the number of elements in `nums` that are not equal to `val`.

The first k elements of `nums` should contain the elements that are not equal to `val`, in any order.
The remaining elements are not important.

Example:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: The function returns k=2, with the first two elements being [2,2]. The underscore
represents any value, as elements beyond k are not considered.

Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

Solution:
This solution uses a two-pointer technique to modify the list in-place. We maintain a pointer `k` for
the position where the next non-val element should go. We iterate through the list, and whenever we find
an element not equal to `val`, we place it at index `k` and increment `k`. This effectively moves all
non-val elements to the front of the list.

Author: [Your Name]
Date: August 18, 2025
"""

def removeElement(nums, val):
    """
    Remove all occurrences of val from nums in-place.
    Args:
        nums (List[int]): List of integers
        val (int): Value to remove
    Returns:
        int: Number of elements not equal to val (k)
    """
    k = 0  # Position for next non-val element
    for i in range(len(nums)):
        if nums[i] != val:  # Found a non-val element
            nums[k] = nums[i]
            k += 1
    return k

# Test cases
test_cases = [
    ([3, 2, 2, 3], 3),       # Example 1: k=2, nums=[2,2,_,_]
    ([0, 1, 2, 2, 3, 0, 4, 2], 2),  # Example 2: k=5, nums=[0,1,3,0,4,_,_,_]
    ([], 1),                  # Empty list: k=0, nums=[]
    ([1], 1),                 # Single element equal to val: k=0, nums=[_]
    ([1, 1, 1], 1),          # All elements equal to val: k=0, nums=[_,_,_]
    ([1, 2, 3], 4)           # No elements equal to val: k=3, nums=[1,2,3]
]

def run_tests():
    """Run test cases and print results."""
    for nums, val in test_cases:
        original = nums.copy()  # Preserve original for display
        k = removeElement(nums, val)
        print(f"Input: nums = {original}, val = {val}")
        print(f"Output: k = {k}, nums = {nums[:k] + ['_'] * (len(nums) - k)}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to remove all occurrences of a given value `val` from a list `nums` in-place, without creating a new list.
   - The order of remaining elements doesn't matter, but I need to return `k`, the count of elements not equal to `val`.
   - The first `k` elements of `nums` should contain all non-val elements.
   - Example: For nums = [3,2,2,3], val = 3, I return k=2 and modify nums to [2,2,_,_].

2. Initial Thoughts:
   - I considered creating a new list to store non-val elements, but the in-place requirement means I must modify `nums` directly.
   - I thought about shifting elements, but that could be complex. Instead, I realized I could overwrite elements at the start of the list.
   - The problem is similar to Remove Duplicates (LeetCode #26), where I used a two-pointer approach, so I decided to try a similar strategy.

3. Two-Pointer Approach:
   - I used two pointers: `k` (position for the next non-val element) and `i` (iteration through the list).
   - Initialize `k=0` to track where to place the next valid element.
   - Iterate `i` from 0 to len(nums)-1. If nums[i] != val, copy nums[i] to nums[k] and increment `k`.
   - This moves all non-val elements to the front of the list, and `k` counts how many there are.
   - Return `k`, as the elements beyond nums[k] are irrelevant.

4. List Operations Used:
   - Indexing: Access nums[i] to check against val and nums[k] to place valid elements.
   - In-place modification: Assign nums[k] = nums[i] to move non-val elements.
   - Iteration: Loop through the list with range(len(nums)).
   - Length check: Use len(nums) to handle empty lists and bounds.

5. Key Insights:
   - The two-pointer technique is efficient (O(n) time, O(1) space) because it only requires one pass and no extra space.
   - Unlike Remove Duplicates, the list isn't sorted, but I don't need to compare adjacent elements—just check against `val`.
   - This approach is like filtering a list in-place, keeping only the elements I want.
   - It connects to my To-Do List Manager project, where I manipulated lists by adding or removing tasks based on conditions.

My Understanding of Remove Element in Real Life:
==============================================
The Remove Element problem has practical applications in scenarios where we need to filter out specific items from a dataset while keeping the operation memory-efficient. Here are some examples:

1. Data Filtering in Spreadsheets:
   - Imagine I'm working with a spreadsheet of sales data, and I need to remove all entries for a specific product ID (e.g., discontinued items).
   - This algorithm helps me filter the list in-place, keeping only relevant data without needing a new spreadsheet, similar to how I modify `nums`.

2. Task Management:
   - In my To-Do List Manager project, I removed tasks by index. This problem is like removing all tasks with a specific status (e.g., "cancelled").
   - The in-place approach ensures I don't waste memory, which is useful for managing large task lists on limited devices.

3. Social Media Moderation:
   - When moderating a sorted list of comments, I might need to remove all comments containing a specific word (e.g., spam).
   - This algorithm allows me to efficiently filter out unwanted comments while keeping the valid ones at the start of the list.

4. Learning Takeaway:
   - This problem taught me how to perform in-place list operations, which is crucial for memory-efficient coding.
   - It builds on my experience with Remove Duplicates and Two Sum, reinforcing the two-pointer technique and list manipulation.
   - In real life, I see this as a way to clean data, like removing spam emails from a mailbox or filtering out irrelevant search results.
   - Solving this prepares me for more complex list problems, like 3Sum, and enhances my algorithmic thinking.

Next Steps:
- I can enhance this by counting the number of elements removed (len(nums) - k).
- I can try a variation, like removing elements that match a condition (e.g., all even numbers).
- Committing this to my GitHub portfolio shows my progress in list manipulation and algorithmic problem-solving.
"""

if __name__ == "__main__":
    run_tests()