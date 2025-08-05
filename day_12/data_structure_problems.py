"""
🎯 Day 12: Data Structure Problem Solving
Big Tech Interview Problems with Multiple Solution Approaches

Today's Focus: Solve common data structure problems efficiently
and understand when to use which data structure for optimal performance.
"""

import collections
import time
from typing import List, Dict, Set, Tuple, Optional

class DataStructureProblemSolver:
    """Solves common data structure problems with multiple approaches."""
    
    def __init__(self):
        """Initialize with test data."""
        self.test_arrays = {
            'duplicates': [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1],
            'two_sum': [2, 7, 11, 15, 3, 6],
            'anagrams': ["eat", "tea", "tan", "ate", "nat", "bat"],
            'sorted': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'unsorted': [64, 34, 25, 12, 22, 11, 90]
        }
    
    def problem_1_find_duplicates(self, arr: List[int]) -> List[int]:
        """
        Problem: Find all duplicates in an array
        Multiple approaches with performance analysis
        """
        print("🔍 === FINDING DUPLICATES ===")
        print(f"Input array: {arr}")
        
        # Approach 1: Using set (O(n) time, O(n) space)
        print("\nApproach 1: Using Set")
        start_time = time.time()
        seen = set()
        duplicates = set()
        for num in arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        set_time = time.time() - start_time
        print(f"Duplicates: {list(duplicates)}")
        print(f"Time: {set_time:.6f}s")
        
        # Approach 2: Using Counter (more Pythonic)
        print("\nApproach 2: Using Counter")
        start_time = time.time()
        counter = collections.Counter(arr)
        duplicates_counter = [num for num, count in counter.items() if count > 1]
        counter_time = time.time() - start_time
        print(f"Duplicates: {duplicates_counter}")
        print(f"Time: {counter_time:.6f}s")
        
        # Approach 3: Using list comprehension with count (O(n²) time)
        print("\nApproach 3: Using count() method")
        start_time = time.time()
        duplicates_count = list(set([x for x in arr if arr.count(x) > 1]))
        count_time = time.time() - start_time
        print(f"Duplicates: {duplicates_count}")
        print(f"Time: {count_time:.6f}s")
        
        print(f"\nPerformance Summary:")
        print(f"Set approach: {set_time:.6f}s (Fastest)")
        print(f"Counter approach: {counter_time:.6f}s")
        print(f"Count method: {count_time:.6f}s (Slowest)")
        
        return list(duplicates)
    
    def problem_2_two_sum(self, nums: List[int], target: int) -> Optional[Tuple[int, int]]:
        """
        Problem: Find two numbers that add up to target
        Classic interview problem with multiple approaches
        """
        print(f"\n🎯 === TWO SUM PROBLEM ===")
        print(f"Array: {nums}")
        print(f"Target: {target}")
        
        # Approach 1: Brute force (O(n²) time, O(1) space)
        print("\nApproach 1: Brute Force")
        start_time = time.time()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    brute_time = time.time() - start_time
                    print(f"Found: indices {i} and {j} (values: {nums[i]}, {nums[j]})")
                    print(f"Time: {brute_time:.6f}s")
                    break
            else:
                continue
            break
        else:
            print("No solution found")
        
        # Approach 2: Using dictionary (O(n) time, O(n) space)
        print("\nApproach 2: Using Dictionary (Optimal)")
        start_time = time.time()
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                dict_time = time.time() - start_time
                print(f"Found: indices {num_dict[complement]} and {i} (values: {complement}, {num})")
                print(f"Time: {dict_time:.6f}s")
                break
            num_dict[num] = i
        else:
            print("No solution found")
        
        # Approach 3: Using set (if we only need to know if solution exists)
        print("\nApproach 3: Using Set (existence check)")
        start_time = time.time()
        seen = set()
        for num in nums:
            complement = target - num
            if complement in seen:
                set_time = time.time() - start_time
                print(f"Solution exists: {complement} + {num} = {target}")
                print(f"Time: {set_time:.6f}s")
                break
            seen.add(num)
        else:
            print("No solution exists")
        
        return None
    
    def problem_3_group_anagrams(self, words: List[str]) -> List[List[str]]:
        """
        Problem: Group anagrams together
        Efficient solution using sorted strings as keys
        """
        print(f"\n📚 === GROUP ANAGRAMS ===")
        print(f"Words: {words}")
        
        # Approach 1: Using defaultdict with sorted string as key
        print("\nApproach 1: Using defaultdict")
        start_time = time.time()
        anagram_groups = collections.defaultdict(list)
        for word in words:
            # Sort characters to create key
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
        
        result = list(anagram_groups.values())
        dict_time = time.time() - start_time
        print(f"Anagram groups: {result}")
        print(f"Time: {dict_time:.6f}s")
        
        # Approach 2: Using Counter as key (more robust for Unicode)
        print("\nApproach 2: Using Counter as key")
        start_time = time.time()
        anagram_groups_counter = collections.defaultdict(list)
        for word in words:
            # Use character count as key
            char_count = tuple(collections.Counter(word).items())
            anagram_groups_counter[char_count].append(word)
        
        result_counter = list(anagram_groups_counter.values())
        counter_time = time.time() - start_time
        print(f"Anagram groups: {result_counter}")
        print(f"Time: {counter_time:.6f}s")
        
        return result
    
    def problem_4_find_missing_number(self, nums: List[int]) -> int:
        """
        Problem: Find missing number in array of 0 to n
        Multiple mathematical approaches
        """
        print(f"\n🔢 === FIND MISSING NUMBER ===")
        print(f"Array (0 to n with one missing): {nums}")
        
        # Approach 1: Using sum formula
        print("\nApproach 1: Using Sum Formula")
        start_time = time.time()
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        missing = expected_sum - actual_sum
        sum_time = time.time() - start_time
        print(f"Missing number: {missing}")
        print(f"Time: {sum_time:.6f}s")
        
        # Approach 2: Using XOR (bit manipulation)
        print("\nApproach 2: Using XOR")
        start_time = time.time()
        result = 0
        for i in range(len(nums)):
            result ^= i ^ nums[i]
        result ^= len(nums)  # XOR with n
        xor_time = time.time() - start_time
        print(f"Missing number: {result}")
        print(f"Time: {xor_time:.6f}s")
        
        # Approach 3: Using set difference
        print("\nApproach 3: Using Set Difference")
        start_time = time.time()
        expected_set = set(range(len(nums) + 1))
        actual_set = set(nums)
        missing_set = expected_set - actual_set
        set_time = time.time() - start_time
        print(f"Missing number: {list(missing_set)[0]}")
        print(f"Time: {set_time:.6f}s")
        
        return missing
    
    def problem_5_longest_consecutive_sequence(self, nums: List[int]) -> int:
        """
        Problem: Find length of longest consecutive sequence
        Efficient O(n) solution using set
        """
        print(f"\n📏 === LONGEST CONSECUTIVE SEQUENCE ===")
        print(f"Array: {nums}")
        
        # Approach 1: Using set for O(n) solution
        print("\nApproach 1: Using Set (Optimal)")
        start_time = time.time()
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Only start counting if this is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        set_time = time.time() - start_time
        print(f"Longest consecutive sequence length: {max_length}")
        print(f"Time: {set_time:.6f}s")
        
        # Approach 2: Using sorting (O(n log n) time)
        print("\nApproach 2: Using Sorting")
        start_time = time.time()
        if not nums:
            return 0
        
        nums_sorted = sorted(nums)
        max_length_sort = 1
        current_length = 1
        
        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i-1] + 1:
                current_length += 1
            elif nums_sorted[i] != nums_sorted[i-1]:
                current_length = 1
            
            max_length_sort = max(max_length_sort, current_length)
        
        sort_time = time.time() - start_time
        print(f"Longest consecutive sequence length: {max_length_sort}")
        print(f"Time: {sort_time:.6f}s")
        
        return max_length
    
    def problem_6_valid_parentheses(self, s: str) -> bool:
        """
        Problem: Check if parentheses are valid
        Classic stack problem
        """
        print(f"\n🔗 === VALID PARENTHESES ===")
        print(f"String: '{s}'")
        
        # Approach 1: Using stack
        print("\nApproach 1: Using Stack")
        start_time = time.time()
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack.pop() != brackets[char]:
                    stack_time = time.time() - start_time
                    print(f"Invalid parentheses")
                    print(f"Time: {stack_time:.6f}s")
                    return False
        
        is_valid = len(stack) == 0
        stack_time = time.time() - start_time
        print(f"Valid parentheses: {is_valid}")
        print(f"Time: {stack_time:.6f}s")
        
        return is_valid
    
    def problem_7_implement_stack_with_queues(self):
        """
        Problem: Implement stack using queues
        Demonstrates data structure conversion
        """
        print(f"\n🔄 === IMPLEMENT STACK WITH QUEUES ===")
        
        class StackUsingQueues:
            def __init__(self):
                self.queue1 = collections.deque()
                self.queue2 = collections.deque()
            
            def push(self, x: int) -> None:
                """Push element onto stack."""
                # Add to queue2
                self.queue2.append(x)
                
                # Move all elements from queue1 to queue2
                while self.queue1:
                    self.queue2.append(self.queue1.popleft())
                
                # Swap the queues
                self.queue1, self.queue2 = self.queue2, self.queue1
            
            def pop(self) -> int:
                """Remove element from top of stack."""
                if self.queue1:
                    return self.queue1.popleft()
                raise IndexError("Stack is empty")
            
            def top(self) -> int:
                """Get top element without removing."""
                if self.queue1:
                    return self.queue1[0]
                raise IndexError("Stack is empty")
            
            def empty(self) -> bool:
                """Check if stack is empty."""
                return len(self.queue1) == 0
        
        # Test the implementation
        stack = StackUsingQueues()
        print("Testing Stack using Queues:")
        
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print(f"After pushing 1, 2, 3: top = {stack.top()}")
        
        print(f"Pop: {stack.pop()}")
        print(f"Pop: {stack.pop()}")
        print(f"Top: {stack.top()}")
        print(f"Empty: {stack.empty()}")
    
    def run_all_problems(self):
        """Run all data structure problems with analysis."""
        print("🚀 === DATA STRUCTURE PROBLEM SOLVING ===")
        print("Solving common Big Tech interview problems...\n")
        
        # Problem 1: Find duplicates
        self.problem_1_find_duplicates(self.test_arrays['duplicates'])
        
        # Problem 2: Two Sum
        self.problem_2_two_sum(self.test_arrays['two_sum'], 9)
        
        # Problem 3: Group Anagrams
        self.problem_3_group_anagrams(self.test_arrays['anagrams'])
        
        # Problem 4: Find Missing Number
        missing_test = [0, 1, 2, 4, 5, 6]  # Missing 3
        self.problem_4_find_missing_number(missing_test)
        
        # Problem 5: Longest Consecutive Sequence
        consecutive_test = [100, 4, 200, 1, 3, 2]
        self.problem_5_longest_consecutive_sequence(consecutive_test)
        
        # Problem 6: Valid Parentheses
        self.problem_6_valid_parentheses("()[]{}")
        self.problem_6_valid_parentheses("([)]")
        
        # Problem 7: Stack with Queues
        self.problem_7_implement_stack_with_queues()
        
        print("\n✅ === ALL PROBLEMS COMPLETED ===")
        print("You've mastered data structure problem solving!")
        print("Ready for Big Tech interview data structure questions!")

# Run the problem solver
if __name__ == "__main__":
    solver = DataStructureProblemSolver()
    solver.run_all_problems() 