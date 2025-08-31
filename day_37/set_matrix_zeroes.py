"""
LeetCode Problem: Set Matrix Zeroes (#73, Medium)
=======================================
Description:
Given an m x n integer matrix `matrix`, if an element is 0, set its entire row and column to 0's. You must do it in-place.

Example:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Explanation: The element at matrix[1][1] is 0, so the entire second row and second column are set to 0.

Constraints:
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -10^9 <= matrix[i][j] <= 10^9

Solution:
This solution uses an in-place marking approach to set rows and columns to zero without extra space (O(1) space excluding temporary variables). We use the first row and first column of the matrix as markers to indicate which rows and columns should be zeroed. A separate flag tracks if the first row needs zeroing. We perform three passes: mark zeros, set zeros based on markers, and handle the first row and column. This ensures O(m*n) time complexity and O(1) space complexity.

Author: [Your Name]
Date: August 31, 2025
"""

def setZeroes(matrix: list[list[int]]) -> None:
    """
    Set entire row and column to 0 for each 0 element in the matrix, in-place.
    Args:
        matrix (List[List[int]]): Input m x n matrix
    """
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = False
    
    # Check if first row has any zero
    for j in range(n):
        if matrix[0][j] == 0:
            first_row_has_zero = True
            break
    
    # Step 1: Use first row and column as markers
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark first cell of row
                matrix[0][j] = 0  # Mark first cell of column
    
    # Step 2: Set zeros for rows (skip first row)
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(n):
                matrix[i][j] = 0
    
    # Step 3: Set zeros for columns (skip first column)
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(m):
                matrix[i][j] = 0
    
    # Step 4: Set first column to zero if needed
    if matrix[0][0] == 0:
        for i in range(m):
            matrix[i][0] = 0
    
    # Step 5: Set first row to zero if needed
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0

# Test cases
test_cases = [
    ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]),  # Example 1: Single zero
    ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]),  # Example 2: Multiple zeros
    ([[1]], [[1]]),  # Single element, no zero
    ([[0]], [[0]]),  # Single element, zero
    ([[1,2,3],[4,0,6],[7,8,9]], [[1,0,3],[0,0,0],[7,0,9]])  # Zero in middle
]

def run_tests():
    """Run test cases and print results."""
    for matrix, expected in test_cases:
        matrix_copy = [row[:] for row in matrix]  # Preserve original for display
        setZeroes(matrix)
        print(f"Input: matrix = {matrix_copy}")
        print(f"Output: {matrix}")
        print(f"Expected: {expected}")
        print(f"Pass: {matrix == expected}\n")

"""
How I Solved It:
================
1. Understanding the Problem:
   - I need to modify an m x n matrix in-place such that if an element is 0, its entire row and column are set to 0.
   - Example: For `matrix = [[1,1,1],[1,0,1],[1,1,1]]`, modify to `[[1,0,1],[0,0,0],[1,0,1]]` due to the 0 at position (1,1).
   - The challenge is to achieve this in-place with O(1) space (excluding temporary variables) and O(m*n) time, given m, n ≤ 200.
   - The matrix is guaranteed to have at least one element, and values are within a wide range.

2. Initial Thoughts:
   - A naive approach could use extra space (e.g., sets to store rows and columns with zeros), but this requires O(m+n) space, violating the in-place requirement.
   - I considered marking cells to be zeroed with a special value, but the wide range of values (-10^9 to 10^9) makes it hard to choose a unique marker.
   - I realized the first row and first column could be used as markers to indicate which rows and columns should be zeroed, with a flag for the first row to avoid conflicts.
   - This approach leverages the matrix itself for storage, achieving O(1) space.

3. In-Place Marking Approach:
   - Steps:
     - Check if the first row has any zeros (store in `first_row_has_zero`).
     - Iterate through the matrix. For each zero at `matrix[i][j]`, mark `matrix[i][0] = 0` (row marker) and `matrix[0][j] = 0` (column marker).
     - Set rows to zero (skip first row) based on `matrix[i][0] == 0`.
     - Set columns to zero (skip first column) based on `matrix[0][j] == 0`.
     - Set the first column to zero if `matrix[0][0] == 0`.
     - Set the first row to zero if `first_row_has_zero` is True.
   - This approach is O(m*n) time (multiple passes over the matrix) and O(1) space (uses only a few variables).
   - It handles all cases, including zeros in the first row/column or single-element matrices.

4. List Operations Used:
   - Matrix indexing: Access `matrix[i][j]`, `matrix[i][0]`, `matrix[0][j]` for marking and setting zeros.
   - In-place modification: Set `matrix[i][j] = 0` for zeroing rows/columns.
   - Iteration: Use nested loops `range(m)` and `range(n)` for scanning and updating.
   - Boolean flag: Use `first_row_has_zero` to track first row status.

5. Key Insights:
   - Using the first row and column as markers eliminates the need for extra space, making the solution truly in-place.
   - Handling the first row separately avoids conflicts when using `matrix[0][0]` as a marker for both row and column.
   - This problem relates to other in-place matrix problems like "Rotate Image" or "Spiral Matrix," but focuses on conditional modification.
   - In a project like an image processor, this could reset pixel rows/columns based on specific conditions (e.g., black pixels).

My Understanding of Set Matrix Zeroes in Real Life:
============================================
The Set Matrix Zeroes problem has practical applications in scenarios involving 2D data modification based on conditions, especially in image processing, data analysis, or game development. Here are some examples:

1. Image Processing:
   - In image editing, this algorithm can reset rows and columns of pixels to zero (e.g., black) based on specific pixel values, useful for masking or filtering.
   - Example: Clearing rows and columns in a grayscale image where a pixel is fully transparent.

2. Data Analysis:
   - In spreadsheet or database processing, this can nullify rows and columns based on missing or invalid data entries.
   - Example: Zeroing out rows/columns in a dataset where a critical value is missing.

3. Game Development:
   - In my To-Do List Manager project, if extended to a grid-based task board, this algorithm could clear rows/columns based on a "cancelled" task marker.
   - Example: Resetting a game board’s row/column when a specific tile is triggered.

4. Learning Takeaway:
   - This problem deepened my understanding of in-place matrix manipulation and marker-based techniques, a pattern seen in "Rotate Image" and "Spiral Matrix."
   - It builds on matrix processing skills from previous problems, preparing me for more complex matrix or array problems.
   - In real life, I see this applying to tasks like processing grid-based data, optimizing memory in embedded systems, or handling sparse matrices.
   - Solving this enhances my ability to design space-efficient algorithms for conditional data modification.

Next Steps:
- I can explore a variation, like setting rows/columns to a different value or handling sparse matrices.
- I can count the number of zeros set to analyze performance.
- Committing this to my GitHub portfolio showcases my skills in in-place matrix manipulation.
- I can explore related problems like "Rotate Image," "Spiral Matrix," or "Game of Life" to further practice matrix techniques.
"""

if __name__ == "__main__":
    run_tests()