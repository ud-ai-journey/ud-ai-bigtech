"""
LeetCode Problem: Merge Sorted Array (#88, Easy)
==============================================
Description:
Given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`,
representing the number of elements in `nums1` and `nums2` respectively, merge `nums2` into `nums1` in-place
such that the resulting array is also sorted in non-decreasing order.

The array `nums1` has a length of m+n, where the first m elements are valid, and the last n elements are
set to 0 and should be ignored. The array `nums2` has a length of n. Modify `nums1` in-place to contain
the merged sorted array.

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: nums1 = [1,2,2,3,5,6]
Explanation: Merge the arrays to form a sorted array in nums1.

Constraints:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[i] <= 10^9

Solution:
This solution uses a two-pointer technique starting from the end of both arrays to merge them in-place.
We compare the largest elements from nums1 and nums2 and place the larger one at the end of nums1,
working backward to avoid overwriting valid elements in nums1. This approach ensures O(1) space complexity
and O(m+n) time complexity.

Author: [Your Name]
Date: August 19, 2025
"""

def merge(nums1, m, nums2, n):
    """
    Merge two sorted arrays in-place into nums1.
    Args:
        nums1 (List[int]): First sorted array with length m+n
        m (int): Number of valid elements in nums1
        nums2 (List[int]): Second sorted array with length n
        n (int): Number of elements in nums2
    """
    p1 = m - 1  # Pointer for nums1
    p2 = n - 1  # Pointer for nums2
    p = m + n - 1  # Pointer for merged array (end of nums1)
    
    while p2 >= 0 and p1 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # If nums2 has remaining elements, copy them
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# Test cases
test_cases = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),  # Example 1: nums1=[1,2,2,3,5,6]
    ([1], 1, [], 0),                          # Single element in nums1: nums1=[1]
    ([], 0, [1], 1),                         # Empty nums1: nums1=[1]
    ([2, 0], 1, [1], 1),                     # Small arrays: nums1=[1,2]
    ([1, 2, 3, 0, 0], 3, [1, 1], 2)          # Overlapping values: nums1=[1,1,1,2,3]
]

def run_tests():
    """Run test cases and print results."""
    for nums1, m, nums2, n in test_cases:
        nums1_copy = nums1.copy()  # Preserve original for display
        merge(nums1, m, nums2, n)
        print(f"Input: nums1 = {nums1_copy}, m = {m}, nums2 = {nums2}, n = {n}")
        print(f"Output: nums1 = {nums1}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to merge two sorted arrays, nums1 and nums2, into nums1 in-place, keeping the result sorted.
   - nums1 has space for m+n elements, but only the first m are valid; the rest are zeros.
   - nums2 has n elements. I modify nums1 to contain the merged sorted array.
   - Example: For nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3, I modify nums1 to [1,2,2,3,5,6].

2. Initial Thoughts:
   - I considered copying nums2 into nums1 (after index m) and sorting nums1, but sorting is O((m+n)log(m+n)).
   - Since both arrays are already sorted, I realized I could merge them efficiently like in the merge step of merge sort.
   - The challenge is doing this in-place without overwriting nums1's valid elements before they're used.

3. Two-Pointer Approach (Backward):
   - I used three pointers: p1 (end of nums1's valid elements, m-1), p2 (end of nums2, n-1), and p (end of nums1, m+n-1).
   - Starting from the end, I compare nums1[p1] and nums2[p2], placing the larger element at nums1[p] and decrementing the corresponding pointer.
   - This works backward to avoid overwriting nums1's valid elements before they're processed.
   - If nums2 has remaining elements (p2 >= 0), I copy them to nums1.
   - If nums1 has remaining elements, they're already in place (since we're working backward).
   - This approach is O(m+n) time and O(1) space since it's in-place.

4. List Operations Used:
   - Indexing: Access nums1[p1], nums2[p2], and assign to nums1[p].
   - In-place modification: Update nums1[p] with the larger element.
   - Iteration: Loop with while conditions (p2 >= 0 and p1 >= 0, then p2 >= 0).
   - Length checks: Use m, n, and m+n to set pointers and bounds.

5. Key Insights:
   - Working backward is key to in-place merging, as it uses the empty space at the end of nums1.
   - The sorted nature of both arrays allows efficient comparison and placement.
   - This is similar to Remove Duplicates and Remove Element, but now I'm merging two lists instead of filtering.
   - It connects to my To-Do List Manager project, where I managed lists and could imagine merging two sorted task lists (e.g., personal and work tasks).

My Understanding of Merge Sorted Array in Real Life:
==================================================
The Merge Sorted Array problem has practical applications in scenarios where we need to combine sorted datasets efficiently while maintaining order. Here are some examples:

1. Database Merging:
   - Imagine I have two sorted lists of customer records (e.g., by ID) from different sources, and I need to merge them into one sorted list.
   - This algorithm allows me to combine them in-place, saving memory, which is useful for large datasets like in a CRM system.

2. Task Scheduling:
   - In my To-Do List Manager project, I could have two sorted lists of tasks (e.g., by deadline) from different categories (work, personal).
   - Merging them in-place into a single sorted list helps me prioritize tasks efficiently without needing extra storage.

3. Social Media Feeds:
   - When combining two sorted feeds (e.g., posts from friends and pages, sorted by timestamp), I can merge them into one sorted feed.
   - Doing this in-place is efficient for real-time applications where memory is limited.

4. Learning Takeaway:
   - This problem taught me how to perform in-place list operations with multiple arrays, enhancing my understanding of memory-efficient coding.
   - It builds on my experience with Remove Duplicates, Remove Element, and Two Sum, reinforcing the two-pointer technique.
   - In real life, I see this as a way to combine ordered data, like merging sorted playlists or combining ranked search results.
   - Solving this prepares me for more complex problems like 3Sum, where I'll handle multiple pointers and conditions.

Next Steps:
- I can enhance this by printing the number of elements moved from nums2.
- I can try a variation, like merging unsorted arrays (requires sorting first).
- Committing this to my GitHub portfolio shows my progress in list manipulation and algorithmic problem-solving.
"""

if __name__ == "__main__":
    run_tests()