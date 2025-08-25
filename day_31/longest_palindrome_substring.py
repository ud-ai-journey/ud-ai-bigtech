"""
LeetCode Problem: Longest Palindromic Substring (#5, Medium)
=======================================
Description:
Given a string `s`, return the longest palindromic substring in `s`. A substring is palindromic if it
reads the same forward and backward. If multiple palindromic substrings have the maximum length,
return any one of them.

Example:
Input: s = "babad"
Output: "bab"
Explanation: "bab" is the longest palindromic substring. "aba" is also valid, but either can be returned.

Constraints:
- 1 <= s.length <= 1000
- s consists of only digits and English letters.

Solution:
This solution uses the expand-around-center approach to find the longest palindromic substring. For each
possible center position in the string, we expand outward to check for palindromes, considering both
odd-length (single character center) and even-length (between two characters) palindromes. We track the
start and end indices of the longest palindrome found. This approach ensures O(n^2) time complexity and
O(1) space complexity, as it only stores a few variables.

Author: [Your Name]
Date: August 25, 2025
"""

def longestPalindrome(s: str) -> str:
    """
    Find the longest palindromic substring in the given string.
    Args:
        s (str): Input string
    Returns:
        str: Longest palindromic substring
    """
    if not s:
        return ""
    
    start, max_length = 0, 1  # Initialize start index and length of longest palindrome
    
    def expand_around_center(left: int, right: int) -> tuple[int, int]:
        """Expand around the center to find the longest palindrome."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the start and length of the palindrome
        return left + 1, right - left - 1
    
    for i in range(len(s)):
        # Check odd-length palindromes (center at i)
        left, length = expand_around_center(i, i)
        if length > max_length:
            start = left
            max_length = length
        
        # Check even-length palindromes (center between i and i+1)
        left, length = expand_around_center(i, i + 1)
        if length > max_length:
            start = left
            max_length = length
    
    return s[start:start + max_length]

# Test cases
test_cases = [
    ("babad", ["bab", "aba"]),           # Example 1: Multiple valid answers
    ("cbbd", ["bb"]),                    # Example 2: Even-length palindrome
    ("a", ["a"]),                        # Single character
    ("racecar", ["racecar"]),            # Entire string is a palindrome
    ("abc", ["a", "b", "c"]),           # No palindrome longer than 1
]

def run_tests():
    """Run test cases and print results."""
    for input_s, expected in test_cases:
        result = longestPalindrome(input_s)
        print(f"Input: s = {input_s}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result in expected}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to find the longest substring in `s` that is a palindrome (reads the same forward and backward).
   - Example: For `s = "babad"`, return "bab" or "aba" (both are valid palindromic substrings of length 3).
   - The challenge is to efficiently check all possible palindromic substrings while handling both odd and even lengths,
     within the constraints of a string length up to 1000.
   - Any valid longest palindrome can be returned if multiple exist.

2. Initial Thoughts:
   - A naive approach could check every possible substring and verify if it’s a palindrome, but this would be O(n^3)
     (O(n^2) substrings, O(n) to check each), which is too slow for n up to 1000.
   - I considered dynamic programming, where `dp[i][j]` indicates if `s[i:j+1]` is a palindrome, but this requires O(n^2)
     space and O(n^2) time, which is less space-efficient.
   - I also thought about checking palindromes from the center outward, as palindromes expand symmetrically around a center.
     This expand-around-center approach seemed promising, as it reduces space complexity to O(1) and maintains O(n^2) time.

3. Expand-Around-Center Approach:
   - I used the expand-around-center technique, where for each index `i`, I treat it as the center of a potential palindrome.
   - There are two cases:
     - Odd-length palindromes: Center at `s[i]`, expand outward (e.g., "aba" with center at 'b').
     - Even-length palindromes: Center between `s[i]` and `s[i+1]`, expand outward (e.g., "bb" with center between two 'b's).
   - For each center, I expand left and right while the characters match and stay within bounds, tracking the longest
     palindrome found by storing its start index and length.
   - After checking all centers (2n-1 possible centers: n for odd, n-1 for even), I return the substring using the start
     index and maximum length.
   - This approach is O(n^2) time (n centers, up to n expansions) and O(1) space (only a few variables).

4. List Operations Used:
   - String indexing: Access `s[left]` and `s[right]` to compare characters.
   - Substring extraction: Use `s[start:start + max_length]` to return the result.
   - Iteration: Loop through indices `i` from 0 to `len(s)-1`.
   - Helper function: `expand_around_center` to handle palindrome expansion and return start index and length.

5. Key Insights:
   - The expand-around-center approach efficiently checks all possible palindromes by leveraging their symmetry, avoiding
     the need to check every substring.
   - Handling both odd and even-length palindromes is critical, as the center can be a single character or between two characters.
   - The approach naturally handles edge cases like single characters (always palindromic) or strings with no palindromes longer
     than one character.
   - This problem relates to other string problems like "Valid Palindrome" or "Palindromic Substrings," but focuses on finding
     the longest substring rather than counting or validating.
   - In a project like a text editor, this could help highlight the longest palindromic text for analysis or formatting.

My Understanding of Longest Palindromic Substring in Real Life:
============================================
The Longest Palindromic Substring problem has practical applications in scenarios involving pattern recognition, text processing,
or data analysis where symmetric structures are important. Here are some examples:

1. Text Processing and Formatting:
   - In a text editor or word processor, identifying the longest palindromic substring can help with formatting or analyzing text
     patterns (e.g., highlighting symmetric phrases in creative writing).
   - Example: A poetry analysis tool could identify palindromic phrases to study linguistic symmetry.

2. DNA Sequence Analysis:
   - In bioinformatics, palindromic sequences in DNA (e.g., "GATATC") are significant because they often indicate restriction
     enzyme sites or structural features. This algorithm can find the longest such sequence efficiently.
   - Example: Identifying palindromic regions in a gene sequence for genetic research.

3. Data Validation and Pattern Matching:
   - In data cleaning, this algorithm can identify symmetric patterns in strings (e.g., in user inputs or logs) to detect errors
     or specific formats.
   - Example: Validating symmetric codes or identifiers in a database.

4. Learning Takeaway:
   - This problem deepened my understanding of string manipulation and the expand-around-center technique, a pattern seen in
     problems like "Palindromic Substrings" or "Manacher’s Algorithm" (an advanced O(n) solution for this problem).
   - It builds on two-pointer techniques from problems like "Valid Palindrome" and prepares me for more complex string problems.
   - In real life, I see this applying to tasks like analyzing text symmetry, processing biological data, or optimizing pattern
     matching in search algorithms.
   - Solving this enhances my ability to design efficient algorithms for string processing in performance-critical applications.

Next Steps:
- I can optimize by exploring Manacher’s Algorithm, which solves this in O(n) time, though it’s more complex.
- I can try a variation, like finding the longest palindromic substring ignoring case or including spaces.
- Committing this to my GitHub portfolio showcases my skills in string manipulation and two-pointer techniques.
- I can explore related problems like "Valid Palindrome," "Palindromic Substrings," or "Shortest Palindrome" to further
  practice string-based algorithms.
"""

if __name__ == "__main__":
    run_tests()