def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    Args:
        s (str): Input string
    Returns:
        int: Length of the longest substring without repeating characters
    """
    char_set = set()  # Track characters in the current window
    left = 0  # Left pointer of the sliding window
    max_length = 0  # Track the maximum length found
    
    for right in range(len(s)):
        # Shrink window until the character at right is not in char_set
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # Add current character to set and update max_length
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
test_cases = [
    ("abcabcbb", 3),    # Example 1: Longest is "abc"
    ("bbbbb", 1),       # Example 2: Longest is "b"
    ("pwwkew", 3),      # Example 3: Longest is "wke"
    ("", 0),            # Empty string
    ("dvdf", 3),        # Longest is "vdf"
    ("aabaab!bb", 3),   # Longest is "ab!" (includes symbols)
]

def run_tests():
    """Run test cases and print results."""
    for input_str, expected in test_cases:
        result = lengthOfLongestSubstring(input_str)
        print(f"Input: s = \"{input_str}\"")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")