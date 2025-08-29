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
    
    start = 0
    max_length = 0
    
    def expand_around_center(left: int, right: int) -> tuple[int, int]:
        """Expand around center to find palindrome length and boundaries."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return length and start index of palindrome
        return right - left - 1, left + 1
    
    for i in range(len(s)):
        # Check odd-length palindrome (center at i)
        length1, start1 = expand_around_center(i, i)
        # Check even-length palindrome (center between i and i+1)
        length2, start2 = expand_around_center(i, i + 1)
        
        # Update if odd-length palindrome is longer
        if length1 > max_length:
            max_length = length1
            start = start1
        # Update if even-length palindrome is longer
        if length2 > max_length:
            max_length = length2
            start = start2
    
    # Return the substring from start to start + max_length
    return s[start:start + max_length]

# Test cases
test_cases = [
    ("babad", ["bab", "aba"]),  # Example 1: "bab" or "aba" are valid
    ("cbbd", ["bb"]),          # Example 2: Only "bb"
    ("a", ["a"]),              # Single character
    ("racecar", ["racecar"]),  # Entire string is a palindrome
    ("abcd", ["a", "b", "c", "d"]),  # No palindromes longer than 1
    ("", [""]),                # Empty string
]

def run_tests():
    """Run test cases and print results."""
    for input_str, expected in test_cases:
        result = longestPalindrome(input_str)
        print(f"Input: s = \"{input_str}\"")
        print(f"Output: \"{result}\"")
        print(f"Expected: {expected}")
        print(f"Pass: {result in expected}\n")

if __name__ == "__main__":
    run_tests()