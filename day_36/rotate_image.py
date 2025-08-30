"""
LeetCode Problem: Rotate Image (#48, Medium)
=======================================
Description:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Explanation: The matrix is rotated 90 degrees clockwise:
- Original: [[1,2,3],[4,5,6],[7,8,9]]
- Rotated: [[7,4,1],[8,5,2],[9,6,3]]

Constraints:
- matrix.length == n
- matrix[i].length == n
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

Solution:
This solution uses a two-step approach to rotate the matrix in-place: first, transpose the matrix (swap elements across the main diagonal), then reverse each row. This achieves the 90-degree clockwise rotation without using extra space. The approach ensures O(n^2) time complexity for an n x n matrix and O(1) space complexity, as it modifies the matrix in-place.

Author: [Your Name]
Date: August 30, 2025
"""

def rotate(matrix: list[list[int]]) -> None:
    """
    Rotate the n x n matrix 90 degrees clockwise in-place.
    Args:
        matrix (List[List[int]]): Input n x n matrix
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix (swap elements across the main diagonal)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Test cases
test_cases = [
    ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),  # Example 1: 3x3 matrix
    ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], 
     [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]),  # Example 2: 4x4 matrix
    ([[1]], [[1]]),  # Single element
    ([[1,2],[3,4]], [[3,1],[4,2]]),  # 2x2 matrix
    ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 
     [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]])  # 4x4 matrix
]

def run_tests():
    """Run test cases and print results."""
    for matrix, expected in test_cases:
        matrix_copy = [row[:] for row in matrix]  # Preserve original for display
        rotate(matrix)
        print(f"Input: matrix = {matrix_copy}")
        print(f"Output: {matrix}")
        print(f"Expected: {expected}")
        print(f"Pass: {matrix == expected}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to rotate an n x n matrix 90 degrees clockwise in-place, modifying the input matrix directly without using extra space.
   - Example: For `matrix = [[1,2,3],[4,5,6],[7,8,9]]`, modify to `[[7,4,1],[8,5,2],[9,6,3]]`.
   - The challenge is to achieve this in-place with O(1) space (excluding temporary variables) and O(n^2) time, given n ≤ 20.
   - The matrix is guaranteed to be square, and elements are within a reasonable range.

2. Initial Thoughts:
   - A naive approach could create a new n x n matrix, fill it with rotated values, and copy back, but this requires O(n^2) extra space, violating the in-place requirement.
   - I observed that a 90-degree clockwise rotation maps element (i,j) to (j,n-1-i). Directly applying this mapping requires a temporary matrix or careful swapping.
   - I considered breaking the rotation into simpler transformations. Rotating 90 degrees clockwise can be achieved by:
     - Transposing the matrix (swapping elements across the main diagonal, i.e., (i,j) ↔ (j,i)).
     - Reversing each row of the transposed matrix.
   - This two-step approach seemed promising, as both steps can be done in-place.

3. Transpose and Reverse Approach:
   - Step 1: Transpose the matrix by swapping elements `matrix[i][j]` with `matrix[j][i]` for `i < j`. This only swaps elements above the main diagonal to avoid double-swapping.
   - Step 2: Reverse each row using Python’s `reverse()` method or manual swapping.
   - Example for `[[1,2,3],[4,5,6],[7,8,9]]`:
     - After transpose: `[[1,4,7],[4,5,8],[7,8,9]]`
     - After row reversal: `[[7,4,1],[8,5,2],[9,6,3]]`
   - This approach is O(n^2) time (O(n^2) for transpose, O(n^2) for row reversals) and O(1) space (only uses temporary variables for swapping).
   - It handles all cases, including 1x1 and 2x2 matrices, without special handling.

4. List Operations Used:
   - Matrix indexing: Access `matrix[i][j]` and `matrix[j][i]` for swapping.
   - Swapping: Use `matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]` for transpose.
   - Row reversal: Use `matrix[i].reverse()` to reverse each row.
   - Iteration: Use nested loops `range(n)` and `range(i, n)` for transpose, and `range(n)` for row reversal.

5. Key Insights:
   - Breaking the rotation into transpose and reverse simplifies the problem and ensures in-place modification.
   - The transpose step only needs to swap elements above the diagonal (i < j) to avoid redundant swaps.
   - This problem relates to other matrix problems like "Spiral Matrix" or "Set Matrix Zeroes," but focuses on in-place transformation.
   - In a project like an image editor, this could rotate pixel data in-place to save memory.

My Understanding of Rotate Image in Real Life:
============================================
The Rotate Image problem has practical applications in scenarios involving 2D data manipulation, especially in graphics, image processing, or game development. Here are some examples:

1. Image Processing:
   - In photo editing software, this algorithm can rotate an image’s pixel matrix 90 degrees clockwise in-place to save memory.
   - Example: Rotating a photo in an editor without creating a new image buffer.

2. Game Development:
   - In 2D games, this can rotate game boards or tile maps (e.g., for puzzles or level design).
   - Example: Rotating a Tetris board or a puzzle grid for gameplay mechanics.

3. Data Transformation:
   - In my To-Do List Manager project, if I extend it to a grid-based task board, this algorithm could rotate the layout for visualization or user preferences.
   - Example: Rotating a dashboard grid to reorient task priorities.

4. Learning Takeaway:
   - This problem deepened my understanding of in-place matrix manipulation and transformation techniques, a pattern seen in "Spiral Matrix" or "Set Matrix Zeroes."
   - It builds on matrix processing skills from "Spiral Matrix" and array skills from "Product of Array Except Self," preparing me for more complex matrix problems.
   - In real life, I see this applying to tasks like rotating UI grids, transforming data matrices, or optimizing memory in embedded systems.
   - Solving this enhances my ability to design space-efficient algorithms for 2D data structures.

Next Steps:
- I can explore rotating the matrix counterclockwise or by 180/270 degrees as variations.
- I can count the number of swaps performed to analyze performance.
- Committing this to my GitHub portfolio showcase my skills in in-place matrix manipulation.
- I can explore related problems like "Spiral Matrix," "Set Matrix Zeroes," or "Transpose Matrix" to further practice matrix techniques.
"""

if __name__ == "__main__":
    run_tests()