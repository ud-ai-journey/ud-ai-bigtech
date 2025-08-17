"""
LeetCode Problem: Remove Duplicates from Sorted Array (#26, Easy)
==============================================================
Description:
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that
each unique element appears only once. The relative order of the elements should be kept the same.
Return the number of unique elements in `nums`.

The first k elements of `nums` should contain the unique elements in their original order, where k is
the number of unique elements. The remaining elements are not important.

Example:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: The function returns k=2, with the first two elements being [1,2]. The underscore
represents any value, as elements beyond k are not considered.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.

Solution:
This solution uses a two-pointer technique to modify the list in-place. We maintain a pointer `k` for
the position where the next unique element should go. We iterate through the list, and whenever we find
a new unique element, we place it at index `k` and increment `k`. Since the list is sorted, duplicates
are adjacent, making it easy to skip them.

Author: [Your Name]
Date: August 17, 2025
"""

def removeDuplicates(nums):
    """
    Remove duplicates from sorted array in-place.
    Args:
        nums (List[int]): Sorted list of integers
    Returns:
        int: Number of unique elements (k)
    """
    if not nums:  # Handle empty list
        return 0
    
    k = 1  # Position for next unique element
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # Found a new unique element
            nums[k] = nums[i]
            k += 1
    
    return k

# Test cases
test_cases = [
    [1, 1, 2],           # Example 1: k=2, nums=[1,2,_]
    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],  # Example 2: k=5, nums=[0,1,2,3,4,_,_,_,_,_]
    [],                  # Empty list: k=0, nums=[]
    [1],                 # Single element: k=1, nums=[1]
    [1, 1, 1]           # All duplicates: k=1, nums=[1,_,_]
]

def run_tests():
    """Run test cases and print results."""
    for nums in test_cases:
        original = nums.copy()  # Preserve original for display
        k = removeDuplicates(nums)
        print(f"Input: nums = {original}")
        print(f"Output: k = {k}, nums = {nums[:k] + ['_'] * (len(nums) - k)}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to remove duplicates from a sorted array in-place, keeping only unique elements in their
     original order.
   - The array is sorted, so duplicates are adjacent (e.g., [1,1,2] means 1's are together).
   - I return `k`, the count of unique elements, and modify `nums` so the first `k` elements are unique.
   - Example: For [1,1,2], I return k=2 and modify nums to [1,2,_].

2. Initial Thoughts:
   - I considered creating a new list with unique elements, but the problem requires in-place
     modification to save space.
   - Since the array is sorted, I can compare adjacent elements to detect duplicates.
   - I need a way to track where to place the next unique element.

3. Two-Pointer Approach:
   - I used two pointers: `k` (position for the next unique element) and `i` (iteration through the list).
   - Start with `k=1` because the first element (nums[0]) is always unique.
   - Iterate `i` from index 1 to the end. If nums[i] != nums[i-1], it's a new unique element.
   - Place nums[i] at nums[k] and increment `k`.
   - This skips duplicates (since nums[i] == nums[i-1] for duplicates) and builds the unique list in-place.
   - Return `k`, the count of unique elements.

4. List Operations Used:
   - Indexing: Access nums[i] and nums[i-1] to compare elements.
   - In-place modification: Assign nums[k] = nums[i] to move unique elements.
   - Iteration: Loop through the list with range(1, len(nums)).
   - Length check: Use len(nums) to determine bounds.

5. Key Insights:
   - The sorted nature of the list makes it easy to detect duplicates by comparing adjacent elements.
   - In-place modification saves space (O(1) space complexity) and is efficient (O(n) time complexity).
   - This approach is like compressing the list by overwriting duplicates with unique elements.
   - It connects to my To-Do List Manager project, where I used lists to manage tasks and indices to
     manipulate them.

My Understanding of Remove Duplicates in Real Life:
=================================================
The Remove Duplicates from Sorted Array problem has practical applications in scenarios where we need to
process or clean data by eliminating redundant entries while preserving order. Here are some examples:

1. Data Cleaning in Databases:
   - Imagine I'm managing a sorted list of customer IDs in a database, but some IDs are duplicated due to
     data entry errors.
   - This algorithm helps me keep only unique IDs in-place, saving memory and maintaining the sorted order.
   - The indices (`k`) tell me how many valid customers remain.

2. Inventory Management:
   - In a warehouse, I might have a sorted list of product codes, but duplicates appear due to scanning
     errors.
   - Removing duplicates in-place ensures I have a clean list of unique products without needing extra
     storage, similar to how this algorithm modifies the array.

3. Social Media Feeds:
   - When displaying a sorted feed of posts (e.g., by timestamp), I might accidentally include duplicate
     posts due to system glitches.
   - This algorithm can filter out duplicates efficiently, ensuring users see only unique content.

4. Learning Takeaway:
   - This problem taught me how to manipulate lists in-place, which is useful for memory-efficient
     coding.
   - It relates to my To-Do List Manager, where I managed tasks in a list and needed to avoid duplicate
     entries (e.g., adding the same task twice).
   - In real life, I see this as a way to streamline data, like removing duplicate contacts in my phone
     or cleaning a playlist of songs.
   - Solving this builds my confidence in handling list operations and prepares me for problems like
     Two Sum or 3Sum, where I also manipulate arrays.

Next Steps:
- I can enhance this by counting the number of duplicates removed (len(nums) - k).
- I can try a variation, like removing duplicates from an unsorted list (harder problem).
- Committing this to my GitHub portfolio shows my progress in list manipulation and algorithmic thinking.
"""

if __name__ == "__main__":
    run_tests()