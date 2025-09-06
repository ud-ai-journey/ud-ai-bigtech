"""
LeetCode Problem: Longest Common Subsequence (#1143, Medium)
=======================================
Description:
Given two strings `text1` and `text2`, return the length of their longest common subsequence. A subsequence is a sequence that can be derived from a string by deleting some or no elements without changing the order of the remaining elements. If there is no common subsequence, return 0.

Example:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace", which has length 3.

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

Solution:
This solution uses a dynamic programming approach to find the length of the longest common subsequence. We create a 2D DP array where `dp[i][j]` represents the length of the LCS for prefixes text1[0:i] and text2[0:j]. If characters match, we add 1 to the LCS of the prefixes without these characters; otherwise, we take the maximum of excluding either character. This ensures O(m*n) time complexity and O(m*n) space complexity, where m and n are the lengths of the input strings.

Author: [Your Name]
Date: September 6, 2025
"""

def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    Find the length of the longest common subsequence between two strings.
    Args:
        text1 (str): First string
        text2 (str): Second string
    Returns:
        int: Length of the longest common subsequence
    """
    m, n = len(text1), len(text2)
    # Initialize DP array with dimensions (m+1) x (n+1) for empty prefixes
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill DP array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

# Test cases
test_cases = [
    (("abcde", "ace"), 3),        # Example 1: Standard case
    (("abc", "abc"), 3),          # Identical strings
    (("abc", "def"), 0),          # No common subsequence
    (("AGGTAB", "GXTXAYB"), 4),   # Example with longer LCS
    (("a", "b"), 0),              # Single characters, no match
]

def run_tests():
    """Run test cases and print results."""
    for (text1, text2), expected in test_cases:
        result = longestCommonSubsequence(text1, text2)
        print(f"Input: text1 = {text1}, text2 = {text2}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to find the length of the longest common subsequence (LCS) between two strings, where a subsequence is formed by deleting elements without changing the order.
   - Example: For `text1 = "abcde"`, `text2 = "ace"`, the LCS is "ace" with length 3.
   - The challenge is to compute this efficiently for strings up to 1000 characters, handling cases with no common subsequence.
   - Only the length is needed, not the subsequence itself.

2. Initial Thoughts:
   - A naive approach could generate all subsequences of both strings and find the longest common one, but this is exponential (O(2^n)), too slow for n ≤ 1000.
   - A recursive approach with memoization could work, but dynamic programming with a 2D table seemed more straightforward for comparing two sequences.
   - I considered a DP array `dp[i][j]` to represent the LCS length for prefixes `text1[0:i]` and `text2[0:j]`.
   - Other approaches like suffix trees or greedy methods were less suitable due to complexity or incorrectness.

3. Dynamic Programming Approach:
   - Define `dp[i][j]` as the length of the LCS for `text1[0:i]` and `text2[0:j]`.
   - If `text1[i-1] == text2[j-1]`, then `dp[i][j] = dp[i-1][j-1] + 1` (include the matching character).
   - Otherwise, `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` (exclude one character and take the maximum).
   - Initialize a (m+1) x (n+1) DP array with zeros to handle empty prefixes.
   - Return `dp[m][n]` as the result.
   - This approach is O(m*n) time (nested loops) and O(m*n) space (DP array).
   - Handles edge cases like identical strings, no common subsequence, or single characters.

4. List Operations Used:
   - 2D array initialization: Create `dp = [[0] * (n + 1) for _ in range(m + 1)]`.
   - String indexing: Access `text1[i-1]` and `text2[j-1]` for comparison.
   - Iteration: Use nested loops `range(1, m + 1)` and `range(1, n + 1)` for DP updates.
   - Maximum: Use `max(dp[i-1][j], dp[i][j-1])` for non-matching cases.

5. Key Insights:
   - The DP approach efficiently builds the LCS by comparing prefixes and reusing subproblem results.
   - The 2D table naturally handles all cases, including no common subsequence (returns 0).
   - This problem relates to "Longest Increasing Subsequence" (DP for subsequences) and "House Robber" (DP optimization).
   - In a project like a text editor, this could measure similarity between two texts for diffing or plagiarism detection.

My Understanding of Longest Common Subsequence in Real Life:
============================================
The Longest Common Subsequence problem has practical applications in scenarios involving sequence comparison, text processing, or bioinformatics. Here are some examples:

1. Text Processing:
   - In version control systems or text editors, this algorithm can compute the similarity between two versions of a document for diffing or merging.
   - Example: Finding the longest common parts of two code files to identify unchanged sections.

2. Bioinformatics:
   - In DNA sequence analysis, this can find the longest common subsequence between two DNA strands to measure similarity.
   - Example: Comparing gene sequences to study evolutionary relationships.

3. Task Optimization:
   - In my To-Do List Manager project, if tasks are represented as sequences (e.g., steps in a process), this algorithm could find common steps between two workflows.
   - Example: Identifying shared tasks between two project plans to streamline collaboration.

4. Learning Takeaway:
   - This problem deepened my understanding of 2D dynamic programming for sequence comparison, a pattern seen in "Longest Increasing Subsequence."
   - It builds on DP skills from "House Robber" and "Coin Change," preparing me for more complex problems like "Edit Distance" or "Longest Palindromic Subsequence."
   - In real life, I see this applying to tasks like text comparison, DNA analysis, or matching ordered data.
   - Solving this enhances my ability to design efficient algorithms for sequence-based problems.

Next Steps:
- I can optimize with space-efficient DP (using a rolling array for O(min(m,n)) space).
- I can explore reconstructing the LCS itself, not just its length.
- Committing this to my GitHub portfolio showcases my skills in dynamic programming and string processing.
- I can explore related problems like "Edit Distance," "Longest Palindromic Subsequence," or "Minimum ASCII Delete Sum for Two Strings" to further practice DP techniques.
"""

if __name__ == "__main__":
    run_tests()