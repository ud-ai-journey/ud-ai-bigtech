"""
LeetCode Problem: Longest Palindromic Substring (#5, Medium)
============================================================
Description:
Given a string s, return the longest palindromic substring in s.

A palindrome is a string that reads the same backward as forward.

Examples:
---------
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

Constraints:
------------
- 1 <= s.length <= 1000
- s consists of only digits and English letters.

Solution Approaches:
--------------------
Approach 1: Dynamic Programming (O(n^2) time, O(n^2) space)
  - dp[i][j] = True if substring s[i:j+1] is palindrome.
  - Base cases:
    - Single chars are palindromes.
    - Two equal chars are palindromes.
  - Expand for length > 2: s[i] == s[j] and dp[i+1][j-1].
  - Track longest.

Approach 2: Expand Around Center (Optimized, O(n^2) time, O(1) space)
  - Every palindrome is centered at one character (odd length) or between two characters (even length).
  - Expand outward while valid.
  - Track max length substring.

We’ll implement **Expand Around Center** for efficiency.

Author: Grok 3
Date: August 24, 2025
"""

def longestPalindrome(s: str) -> str:
    """
    Return the longest palindromic substring in s.
    Args:
        s (str): Input string.
    Returns:
        str: Longest palindrome substring.
    """
    if len(s) <= 1:
        return s
    
    start, end = 0, 0
    
    def expandAroundCenter(left: int, right: int) -> tuple[int, int]:
        """Expand around center and return final bounds."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1
    
    for i in range(len(s)):
        # Odd-length palindrome
        l1, r1 = expandAroundCenter(i, i)
        # Even-length palindrome
        l2, r2 = expandAroundCenter(i, i+1)
        
        # Pick longer palindrome
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2
    
    return s[start:end+1]

# ------------------- Test Cases -------------------
test_cases = [
    ("babad", ["bab","aba"]),  # Multiple correct answers
    ("cbbd", ["bb"]),
    ("a", ["a"]),
    ("ac", ["a","c"]),
    ("forgeeksskeegfor", ["geeksskeeg"]),  # Longer palindrome
]

def run_tests():
    """Run test cases and print results."""
    for s, expected_options in test_cases:
        result = longestPalindrome(s)
        print(f"Input: {s}")
        print(f"Output: {result}")
        print(f"Expected One Of: {expected_options}")
        print(f"Pass: {result in expected_options}\n")

"""
How I Solved It:
================
1. Understanding:
   - Need longest substring palindrome (contiguous).
   - Example: "babad" → "bab" or "aba".

2. Thoughts:
   - Brute force: check all substrings → O(n^3).
   - DP: store palindrome validity → O(n^2).
   - Expand Around Center: O(n^2) but O(1) space.

3. Algorithm (Expand Around Center):
   - For each index, try expanding:
     - Odd-length center at i.
     - Even-length center at (i, i+1).
   - Track longest expansion.

4. Key Insights:
   - Every palindrome has a "center".
   - Expand until mismatch.
   - Compare lengths to update answer.

Real-Life Applications:
=======================
1. DNA / Genome Analysis:
   - Palindromic sequences have biological importance.

2. Text Processing:
   - Detect palindromic patterns in words or logs.

3. Data Compression:
   - Repeated symmetric structures can be optimized.

4. Cryptography:
   - Palindromic keys or structures in encoding/decoding.

Learning Takeaway:
------------------
- DP and Expand Around Center are standard approaches for substring problems.
- Expand Around Center is space-efficient compared to DP.
- Builds intuition for harder problems:
  - "Palindromic Substrings" (#647)
  - "Longest Palindromic Subsequence" (#516)

Next Steps:
-----------
- Try Manacher’s Algorithm (O(n)) for advanced optimization.
- Extend to "longest palindrome subsequence" (non-contiguous).
- Commit to GitHub for showcasing DP + center expansion mastery.
"""

if __name__ == "__main__":
    run_tests()