"""
LeetCode Problem: Group Anagrams (#49, Medium)
=======================================
Description:
Given an array of strings `strs`, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of another, such as "cinema" and "iceman". You can return the answer in any order. Anagrams should be grouped into lists, and the result should be a list of these groups.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
Explanation: The strings are grouped by anagrams:
- "eat", "tea", "ate" are anagrams (same letters: e, a, t).
- "tan", "nat" are anagrams (same letters: t, a, n).
- "bat" is its own group (no other anagrams).

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

Solution:
This solution uses a hash map to group anagrams by their sorted character strings. For each string in `strs`, we sort its characters to create a key (since anagrams have the same sorted characters). We then use this key to group the original strings in a hash map. Finally, we return the values of the hash map as a list of lists. This approach ensures O(n * k * log k) time complexity, where n is the length of `strs` and k is the maximum length of a string, with O(n * k) space complexity for the hash map.

Author: Grok 3
Date: August 23, 2025
"""

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    Group anagrams together from an array of strings.
    Args:
        strs (List[str]): Array of strings
    Returns:
        List[List[str]]: List of grouped anagrams
    """
    anagram_map = {}
    
    for s in strs:
        # Sort the characters of the string to create a key
        sorted_str = ''.join(sorted(s))
        # Add the original string to the list corresponding to the sorted key
        if sorted_str not in anagram_map:
            anagram_map[sorted_str] = []
        anagram_map[sorted_str].append(s)
    
    # Return the grouped anagrams as a list of lists
    return list(anagram_map.values())

# Test cases
test_cases = [
    (["eat","tea","tan","ate","nat","bat"], 
     [["eat","tea","ate"],["tan","nat"],["bat"]]),  # Example 1: Mixed anagrams
    ([""], [[""]]),                                 # Single empty string
    (["a"], [["a"]]),                               # Single character string
    (["cab","bac","abc"], [["cab","bac","abc"]]),  # All anagrams
    (["rat","tar","art","cat"], 
     [["rat","tar","art"],["cat"]]),               # Multiple groups
]

def run_tests():
    """Run test cases and print results."""
    for input_strs, expected in test_cases:
        input_copy = input_strs.copy()  # Preserve original for display
        result = groupAnagrams(input_strs)
        # Sort results and expected for consistent comparison
        result = [sorted(group) for group in sorted(result, key=lambda x: sorted(x[0]))]
        expected = [sorted(group) for group in sorted(expected, key=lambda x: sorted(x[0]))]
        print(f"Input: strs = {input_copy}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to group strings from the input array `strs` that are anagrams of each other.
   - Example: For `strs = ["eat","tea","tan","ate","nat","bat"]`, group into `[["eat","tea","ate"],["tan","nat"],["bat"]]`.
   - The challenge is to efficiently identify anagrams and group them, handling edge cases like empty strings or single-character strings.
   - The output order of groups and strings within groups doesn't matter, but the grouping must be correct.

2. Initial Thoughts:
   - A naive approach could compare each string with every other string by sorting their characters (O(n^2 * k * log k)), but this is too slow for n up to 10^4.
   - I considered counting characters (e.g., using a frequency array of 26 lowercase letters) for each string to create a key, which would be O(n * k) but requires converting counts to a hashable key.
   - Sorting each string's characters to use as a hash map key seemed intuitive, as anagrams have identical sorted strings.
   - A hash map approach with sorted strings as keys allows grouping in one pass, balancing simplicity and efficiency.

3. Hash Map with Sorted Strings Approach:
   - I used a hash map (`anagram_map`) where the key is the sorted version of a string, and the value is a list of original strings that are anagrams.
   - For each string `s` in `strs`:
     - Sort its characters to create a key (e.g., "eat" → "aet").
     - Add the original string to the list in `anagram_map[sorted_str]`.
   - After processing all strings, return the values of the hash map as a list of lists.
   - This approach is O(n * k * log k) due to sorting each string of length k, and O(n * k) space for storing the strings in the hash map.

4. List Operations Used:
   - String sorting: `''.join(sorted(s))` to create a sorted string key.
   - Hash map operations: Check if a key exists (`sorted_str not in anagram_map`), initialize lists (`anagram_map[sorted_str] = []`), and append strings (`anagram_map[sorted_str].append(s)`).
   - Iteration: Loop through `strs` with a for loop.
   - Return values: Use `list(anagram_map.values())` to get the grouped anagrams.

5. Key Insights:
   - Sorting characters is a reliable way to identify anagrams, as anagrams have the same characters in a different order.
   - Using a hash map allows grouping in one pass, avoiding the need for pairwise comparisons.
   - The approach handles edge cases (empty strings, single characters) naturally, as sorting an empty string gives an empty string, and single characters are their own sorted form.
   - This problem relates to other string manipulation problems like "Valid Anagram" or "Find All Anagrams in a String," but focuses on grouping rather than validation or searching.
   - In a project like a text processing tool, this could group words by their anagrams for tasks like spell-checking or word game solvers.

My Understanding of Group Anagrams in Real Life:
============================================
The Group Anagrams problem has practical applications in scenarios where data needs to be grouped by equivalence under some transformation, such as in text processing or data organization. Here are some examples:

1. Text Processing and Search:
   - In a search engine or spell-checker, grouping anagrams can help suggest related words (e.g., suggesting "tea" when searching for "eat").
   - Example: A crossword puzzle solver could group dictionary words by their anagrams to find valid words for a given set of letters.

2. Data Deduplication:
   - In data cleaning, this algorithm can group records that are equivalent under some transformation (e.g., names with rearranged letters, like "Tom Marvolo Riddle" and "I am Lord Voldemort").
   - This helps identify duplicates in datasets with permuted entries.

3. Word Games and Education:
   - In my To-Do List Manager project, if I extend it to a word game or vocabulary app, grouping anagrams could help generate challenges (e.g., "Find all words that are anagrams of 'listen'").
   - This could enhance learning tools by grouping words with similar letters for practice.

4. Learning Takeaway:
   - This problem strengthened my understanding of hash maps for grouping data based on a computed key, a pattern seen in problems like "Group Shifted Strings" or "Subarray Sum Equals K."
   - It builds on string manipulation techniques from problems like "Valid Anagram" and prepares me for more complex grouping tasks.
   - In real life, I see this applying to tasks like organizing inventory by equivalent items, clustering search queries, or grouping social media posts by similar content.
   - Solving this enhances my ability to design efficient algorithms for grouping and categorizing data in memory-constrained or performance-critical systems.

Next Steps:
- I can optimize by using a character count array (26 lowercase letters) as a key instead of sorting, reducing time complexity to O(n * k) at the cost of more complex key generation.
- I can try a variation, like grouping anagrams with a limited number of groups or handling case-insensitive anagrams.
- Committing this to my GitHub portfolio showcases my skills in string manipulation and hash map usage.
- I can explore related problems like "Valid Anagram," "Find All Anagrams in a String," or "Group Shifted Strings" to deepen my understanding of string-based algorithms.
"""

if __name__ == "__main__":
    run_tests()