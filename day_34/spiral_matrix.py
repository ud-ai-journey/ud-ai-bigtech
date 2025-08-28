"""
LeetCode Problem: Spiral Matrix (#54, Medium)
=======================================
Description:
Given an m x n matrix, return all elements of the matrix in spiral order (clockwise from the top-left corner). The spiral order starts from the top-left, moves right, then down, left, and up, continuing inward until all elements are visited.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Explanation: The elements are traversed in a clockwise spiral order:
- Right: 1,2,3
- Down: 6,9
- Left: 8,7
- Up: 4,5

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

Solution:
This solution uses a boundary tracking approach to traverse the matrix in a spiral order. We maintain four pointers (top, right, bottom, left) to represent the boundaries of the unvisited portion of the matrix. We traverse right, down, left, and up within these boundaries, shrinking them after each direction is completed, until all elements are visited. This ensures O(m*n) time complexity and O(1) space complexity (excluding the output array).

Author: [Your Name]
Date: August 28, 2025
"""

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    """
    Return all elements of the matrix in spiral order.
    Args:
        matrix (List[List[int]]): Input matrix
    Returns:
        List[int]: Elements in spiral order
    """
    if not matrix or not matrix[0]:
        return []
    
    m, n = len(matrix), len(matrix[0])
    result = []
    top, bottom = 0, m - 1
    left, right = 0, n - 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        # Traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Traverse left
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        
        if left <= right:
            # Traverse up
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

# Test cases
test_cases = [
    ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),  # Example 1: 3x3 matrix
    ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),  # Example 2: 3x4 matrix
    ([[1]], [1]),  # Single element
    ([[1,2],[3,4]], [1,2,4,3]),  # 2x2 matrix
    ([], []),  # Empty matrix
]

def run_tests():
    """Run test cases and print results."""
    for matrix, expected in test_cases:
        matrix_copy = [row[:] for row in matrix]  # Preserve original for display
        result = spiralOrder(matrix)
        print(f"Input: matrix = {matrix_copy}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to return a list of all elements in a matrix traversed in a clockwise spiral order, starting from the top-left.
   - Example: For `matrix = [[1,2,3],[4,5,6],[7,8,9]]`, return `[1,2,3,6,9,8,7,4,5]`.
   - The challenge is to traverse the matrix in a spiral pattern efficiently, handling edge cases like single-element or empty matrices, within the constraints of m, n ≤ 10.
   - The solution must visit each element exactly once and produce the correct order.

2. Initial Thoughts:
   - A naive approach could use a visited matrix to track seen elements and change directions manually, but this requires O(m*n) extra space.
   - I considered simulating the spiral by maintaining a direction variable (right, down, left, up) and turning when hitting a boundary, but managing direction changes is error-prone.
   - Using boundary pointers (top, right, bottom, left) to define the unvisited portion seemed intuitive, as the spiral naturally shrinks inward after each direction.
   - This boundary tracking approach avoids extra space and simplifies the logic by processing each direction separately.

3. Boundary Tracking Approach:
   - I used four pointers: `top` (first unvisited row), `bottom` (last unvisited row), `left` (first unvisited column), and `right` (last unvisited column).
   - Steps:
     - Traverse right along the top row, increment `top`.
     - Traverse down along the right column, decrement `right`.
     - If `top <= bottom`, traverse left along the bottom row, decrement `bottom`.
     - If `left <= right`, traverse up along the left column, increment `left`.
     - Repeat until `top > bottom` or `left > right`.
   - The checks `top <= bottom` and `left <= right` prevent revisiting elements in single-row or single-column cases.
   - This approach is O(m*n) time (visits each element once) and O(1) space (excluding the output array).

4. List Operations Used:
   - Matrix indexing: Access `matrix[i][j]` for traversal.
   - List appending: Add elements to `result` with `result.append(matrix[i][j])`.
   - Iteration: Use `range(left, right + 1)` for right, `range(top, bottom + 1)` for down, etc.
   - Boundary updates: Increment/decrement `top`, `bottom`, `left`, `right`.

5. Key Insights:
   - The boundary tracking approach ensures all elements are visited in the correct order without extra space, making it efficient for the constraints.
   - Conditional checks (`top <= bottom` and `left <= right`) handle edge cases like 1xN or Mx1 matrices, preventing duplicate or missed elements.
   - This problem relates to other matrix problems like "Rotate Matrix" or "Set Matrix Zeroes," but focuses on traversal order.
   - In a project like a graphics editor, this could simulate spiral rendering of pixels or data points.

My Understanding of Spiral Matrix in Real Life:
============================================
The Spiral Matrix problem has practical applications in scenarios involving 2D data traversal or rendering, especially in graphics, gaming, or data processing. Here are some examples:

1. Graphics and Rendering:
   - In image processing or graphics, this algorithm can traverse pixels in a spiral order for effects like inward spirals or animations.
   - Example: Rendering a spiral pattern in a game’s visual effect or UI animation.

2. Data Serialization:
   - In data processing, this can serialize a 2D dataset (e.g., spreadsheet or grid) into a 1D array in a specific order for analysis or storage.
   - Example: Converting a 2D sensor grid into a 1D stream for transmission.

3. Game Development:
   - In my To-Do List Manager project, if I extend it to a grid-based interface (e.g., task board), this algorithm could display tasks in a spiral order for visualization.
   - Example: Traversing a game board in a spiral to process tiles or reveal elements.

4. Learning Takeaway:
   - This problem deepened my understanding of matrix manipulation and boundary tracking, a pattern seen in problems like "Rotate Matrix" or "Matrix Diagonal Traverse."
   - It builds on array processing skills from "Sort Colors" and "Product of Array Except Self," preparing me for more complex matrix problems.
   - In real life, I see this applying to tasks like rendering UI elements, processing grid-based data, or simulating spiral patterns in simulations.
   - Solving this enhances my ability to design efficient algorithms for 2D data structures.

Next Steps:
- I can optimize by handling larger matrices or exploring a direction-based approach (right, down, left, up) with a direction array.
- I can try a variation, like traversing in a counterclockwise spiral or handling non-rectangular matrices.
- Committing this to my GitHub portfolio showcases my skills in matrix manipulation and boundary tracking.
- I can explore related problems like "Rotate Matrix," "Matrix Diagonal Traverse," or "Set Matrix Zeroes" to further practice matrix techniques.
"""

if __name__ == "__main__":
    run_tests()