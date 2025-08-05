"""
🔧 Day 12: Data Structures & Collections Mastery
The Data Architect's Toolkit - From Lists to Advanced Collections

Today's Mission: Master Python's built-in data structures and collections
for efficient data manipulation and Big Tech interview preparation.
"""

import collections
from typing import List, Dict, Set, Tuple, Any
import time

class DataStructuresMaster:
    """Master class for all data structure operations and optimizations."""
    
    def __init__(self):
        """Initialize with sample data for demonstrations."""
        self.sample_list = [1, 2, 3, 4, 5, 2, 3, 4, 5, 6]
        self.sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.sample_set = {1, 2, 3, 4, 5}
        self.sample_tuple = (1, 2, 3, 4, 5)
        
    def demonstrate_list_operations(self):
        """Comprehensive list operations with performance analysis."""
        print("📋 === LIST OPERATIONS MASTERY ===")
        
        # 1. List Creation and Basic Operations
        numbers = [1, 2, 3, 4, 5]
        print(f"Original list: {numbers}")
        
        # 2. List Comprehension (Pythonic way)
        squares = [x**2 for x in numbers]
        print(f"Squares using comprehension: {squares}")
        
        # 3. Filtering with comprehension
        even_squares = [x**2 for x in numbers if x % 2 == 0]
        print(f"Even squares: {even_squares}")
        
        # 4. List slicing and manipulation
        print(f"First 3 elements: {numbers[:3]}")
        print(f"Last 3 elements: {numbers[-3:]}")
        print(f"Every 2nd element: {numbers[::2]}")
        
        # 5. Performance comparison: append vs extend
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        
        # Method 1: Append (adds as single element)
        list1_append = list1.copy()
        list1_append.append(list2)
        print(f"Append result: {list1_append}")
        
        # Method 2: Extend (adds each element)
        list1_extend = list1.copy()
        list1_extend.extend(list2)
        print(f"Extend result: {list1_extend}")
        
        # 6. Advanced list operations
        mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
        print(f"Mixed data types: {mixed_list}")
        
        # 7. List performance optimization
        large_list = list(range(10000))
        start_time = time.time()
        sum_result = sum(large_list)
        end_time = time.time()
        print(f"Sum of 10k numbers: {sum_result} (Time: {end_time - start_time:.6f}s)")
        
    def demonstrate_tuple_operations(self):
        """Tuple operations - immutable but efficient."""
        print("\n📦 === TUPLE OPERATIONS ===")
        
        # 1. Tuple creation and immutability
        coordinates = (10, 20)
        print(f"Coordinates: {coordinates}")
        
        # 2. Tuple unpacking
        x, y = coordinates
        print(f"Unpacked: x={x}, y={y}")
        
        # 3. Named tuples (from collections)
        Point = collections.namedtuple('Point', ['x', 'y'])
        point = Point(10, 20)
        print(f"Named tuple: {point}")
        print(f"Access by name: x={point.x}, y={point.y}")
        
        # 4. Tuple performance vs list
        large_tuple = tuple(range(10000))
        large_list = list(range(10000))
        
        # Memory efficiency comparison
        import sys
        tuple_size = sys.getsizeof(large_tuple)
        list_size = sys.getsizeof(large_list)
        print(f"Tuple memory: {tuple_size} bytes")
        print(f"List memory: {list_size} bytes")
        print(f"Memory savings: {list_size - tuple_size} bytes")
        
    def demonstrate_set_operations(self):
        """Set operations for unique data and mathematical operations."""
        print("\n🎯 === SET OPERATIONS ===")
        
        # 1. Basic set operations
        set1 = {1, 2, 3, 4, 5}
        set2 = {4, 5, 6, 7, 8}
        print(f"Set 1: {set1}")
        print(f"Set 2: {set2}")
        
        # 2. Mathematical set operations
        union = set1 | set2
        intersection = set1 & set2
        difference = set1 - set2
        symmetric_diff = set1 ^ set2
        
        print(f"Union: {union}")
        print(f"Intersection: {intersection}")
        print(f"Difference (set1 - set2): {difference}")
        print(f"Symmetric difference: {symmetric_diff}")
        
        # 3. Set comprehension
        even_set = {x for x in range(10) if x % 2 == 0}
        print(f"Even numbers set: {even_set}")
        
        # 4. Performance: Set vs List for membership testing
        large_set = set(range(10000))
        large_list = list(range(10000))
        
        # Test membership performance
        target = 5000
        start_time = time.time()
        in_set = target in large_set
        set_time = time.time() - start_time
        
        start_time = time.time()
        in_list = target in large_list
        list_time = time.time() - start_time
        
        print(f"Set membership test: {set_time:.6f}s")
        print(f"List membership test: {list_time:.6f}s")
        if set_time > 0:
            print(f"Set is {list_time/set_time:.1f}x faster for membership!")
        else:
            print("Set membership test was too fast to measure accurately!")
        
    def demonstrate_dict_operations(self):
        """Dictionary operations for key-value data management."""
        print("\n🗂️ === DICTIONARY OPERATIONS ===")
        
        # 1. Dictionary creation and manipulation
        person = {
            'name': 'Alice',
            'age': 30,
            'city': 'New York',
            'skills': ['Python', 'JavaScript', 'SQL']
        }
        print(f"Person data: {person}")
        
        # 2. Dictionary comprehension
        squares_dict = {x: x**2 for x in range(5)}
        print(f"Squares dictionary: {squares_dict}")
        
        # 3. Advanced dictionary operations
        # Merge dictionaries
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        merged = {**dict1, **dict2}
        print(f"Merged dictionaries: {merged}")
        
        # 4. DefaultDict for counting
        words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
        word_count = collections.defaultdict(int)
        for word in words:
            word_count[word] += 1
        print(f"Word frequency: {dict(word_count)}")
        
        # 5. OrderedDict for maintaining insertion order
        ordered_dict = collections.OrderedDict()
        ordered_dict['first'] = 1
        ordered_dict['second'] = 2
        ordered_dict['third'] = 3
        print(f"OrderedDict: {ordered_dict}")
        
        # 6. Dictionary performance optimization
        large_dict = {i: i**2 for i in range(10000)}
        
        # Key lookup performance
        target_key = 5000
        start_time = time.time()
        value = large_dict.get(target_key, None)
        dict_time = time.time() - start_time
        print(f"Dictionary lookup: {dict_time:.6f}s")
        
    def demonstrate_collections_module(self):
        """Advanced collections for specialized data structures."""
        print("\n🔧 === COLLECTIONS MODULE MASTERY ===")
        
        # 1. Counter for frequency analysis
        text = "hello world hello python world"
        word_freq = collections.Counter(text.split())
        print(f"Word frequency: {word_freq}")
        print(f"Most common: {word_freq.most_common(2)}")
        
        # 2. Deque for efficient queue/stack operations
        dq = collections.deque([1, 2, 3, 4, 5])
        print(f"Original deque: {dq}")
        
        dq.appendleft(0)  # O(1) operation
        dq.append(6)      # O(1) operation
        print(f"After operations: {dq}")
        
        # 3. ChainMap for multiple dictionaries
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        chain = collections.ChainMap(dict1, dict2)
        print(f"ChainMap: {dict(chain)}")
        
        # 4. NamedTuple for structured data
        Employee = collections.namedtuple('Employee', ['name', 'age', 'department'])
        emp = Employee('John', 30, 'Engineering')
        print(f"Employee: {emp}")
        print(f"Employee name: {emp.name}")
        
    def solve_interview_problems(self):
        """Common data structure interview problems."""
        print("\n🎯 === INTERVIEW PROBLEMS ===")
        
        # Problem 1: Find duplicates in array
        print("Problem 1: Find duplicates efficiently")
        arr = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
        
        # Method 1: Using set (O(n) time, O(n) space)
        seen = set()
        duplicates = set()
        for num in arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        print(f"Duplicates (set method): {duplicates}")
        
        # Method 2: Using Counter (more Pythonic)
        counter = collections.Counter(arr)
        duplicates_counter = [num for num, count in counter.items() if count > 1]
        print(f"Duplicates (Counter method): {duplicates_counter}")
        
        # Problem 2: Two Sum (find pair that sums to target)
        print("\nProblem 2: Two Sum")
        nums = [2, 7, 11, 15, 3, 6]
        target = 9
        
        # Efficient solution using dictionary
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                print(f"Two Sum found: {num_dict[complement]} and {i}")
                break
            num_dict[num] = i
        else:
            print("No two sum found")
            
        # Problem 3: Group anagrams
        print("\nProblem 3: Group Anagrams")
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        
        anagram_groups = collections.defaultdict(list)
        for word in words:
            # Sort characters to create key
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
        
        result = list(anagram_groups.values())
        print(f"Anagram groups: {result}")
        
    def performance_analysis(self):
        """Compare performance of different data structures."""
        print("\n⚡ === PERFORMANCE ANALYSIS ===")
        
        # Test data
        size = 100000
        test_data = list(range(size))
        
        # List operations
        start_time = time.time()
        test_list = list(test_data)
        list_creation = time.time() - start_time
        
        start_time = time.time()
        test_list.append(999999)
        list_append = time.time() - start_time
        
        # Set operations
        start_time = time.time()
        test_set = set(test_data)
        set_creation = time.time() - start_time
        
        start_time = time.time()
        test_set.add(999999)
        set_add = time.time() - start_time
        
        # Dictionary operations
        start_time = time.time()
        test_dict = {i: i for i in test_data}
        dict_creation = time.time() - start_time
        
        start_time = time.time()
        test_dict[999999] = 999999
        dict_add = time.time() - start_time
        
        print("Performance Comparison (100k elements):")
        print(f"List creation: {list_creation:.6f}s")
        print(f"Set creation: {set_creation:.6f}s")
        print(f"Dict creation: {dict_creation:.6f}s")
        print(f"List append: {list_append:.6f}s")
        print(f"Set add: {set_add:.6f}s")
        print(f"Dict add: {dict_add:.6f}s")
        
    def run_demonstrations(self):
        """Run all demonstrations in sequence."""
        print("🚀 === DATA STRUCTURES MASTERY DEMONSTRATION ===\n")
        
        self.demonstrate_list_operations()
        self.demonstrate_tuple_operations()
        self.demonstrate_set_operations()
        self.demonstrate_dict_operations()
        self.demonstrate_collections_module()
        self.solve_interview_problems()
        self.performance_analysis()
        
        print("\n✅ === DATA STRUCTURES MASTERY COMPLETE ===")
        print("You've mastered Python's core data structures!")
        print("Ready for Big Tech interview data structure questions!")

# Interactive demonstration
if __name__ == "__main__":
    master = DataStructuresMaster()
    master.run_demonstrations() 