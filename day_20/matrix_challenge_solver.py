class MatrixChallengeSolver:
    def __init__(self):
        """Initialize empty matrices for storing inputs."""
        self.matrix1 = []
        self.matrix2 = []

    def create_2d_list(self, rows, cols, prompt="Enter numbers"):
        """Create a 2D list with user-input values."""
        try:
            rows, cols = int(rows), int(cols)
            if rows < 1 or cols < 1:
                print("Rows and columns must be positive.")
                return []
            print(f"{prompt} for a {rows}x{cols} matrix (row-wise, comma-separated):")
            values = input().split(",")
            if len(values) != rows * cols:
                print(f"Expected {rows * cols} numbers, got {len(values)}.")
                return []
            return [[int(values[i * cols + j]) for j in range(cols)] for i in range(rows)]
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            return []

    def print_2d_list(self, matrix, message="Matrix"):
        """Print a 2D list in a readable format."""
        if not matrix:
            print("Matrix is empty.")
        else:
            print(message + ":")
            for row in matrix:
                print(" ".join(map(str, row)))

    def matrix_multiplication(self, matrix1, matrix2):
        """Compute the product of two matrices if compatible."""
        if not matrix1 or not matrix2 or not matrix1[0] or not matrix2[0]:
            return []
        rows1, cols1 = len(matrix1), len(matrix1[0])
        rows2, cols2 = len(matrix2), len(matrix2[0])
        if cols1 != rows2:
            print("Matrices are not compatible for multiplication.")
            return []
        result = [[0 for _ in range(cols2)] for _ in range(rows1)]
        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        return result

    def extract_border_elements(self, matrix):
        """Extract border elements in clockwise order starting from top-left."""
        if not matrix or not matrix[0]:
            return []
        result = []
        rows, cols = len(matrix), len(matrix[0])
        if rows == 1:
            return matrix[0]
        if cols == 1:
            return [matrix[i][0] for i in range(rows)]
        # Top row
        for j in range(cols):
            result.append(matrix[0][j])
        # Right column (exclude top-right corner)
        for i in range(1, rows):
            result.append(matrix[i][cols - 1])
        # Bottom row (exclude bottom-right corner)
        if rows > 1:
            for j in range(cols - 2, -1, -1):
                result.append(matrix[rows - 1][j])
        # Left column (exclude bottom-left and top-left corners)
        if cols > 1:
            for i in range(rows - 2, 0, -1):
                result.append(matrix[i][0])
        return result

    def find_max_element(self, matrix):
        """Find the maximum element and its position (row, col)."""
        if not matrix or not matrix[0]:
            return None, (-1, -1)
        max_val = matrix[0][0]
        max_pos = (0, 0)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > max_val:
                    max_val = matrix[i][j]
                    max_pos = (i, j)
        return max_val, max_pos

    def display_menu(self):
        """Display the interactive menu."""
        print("\nMatrix Challenge Solver Menu:")
        print("1. Matrix Multiplication")
        print("2. Extract Border Elements")
        print("3. Find Maximum Element and Position")
        print("4. Print Current Matrices")
        print("0. Exit")

    def run(self):
        """Run the interactive menu."""
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice (0-4): "))
                if choice == 0:
                    print("Exiting...")
                    break
                if choice not in range(1, 5):
                    print("Invalid choice. Please select 0-4.")
                    continue
                if choice == 1:
                    rows1 = input("Enter number of rows for first matrix: ")
                    cols1 = input("Enter number of columns for first matrix: ")
                    self.matrix1 = self.create_2d_list(rows1, cols1, "Enter numbers for first matrix")
                    if not self.matrix1:
                        continue
                    rows2 = input("Enter number of rows for second matrix: ")
                    cols2 = input("Enter number of columns for second matrix: ")
                    self.matrix2 = self.create_2d_list(rows2, cols2, "Enter numbers for second matrix")
                    if not self.matrix2:
                        continue
                    result = self.matrix_multiplication(self.matrix1, self.matrix2)
                    if result:
                        self.print_2d_list(self.matrix1, "First matrix")
                        self.print_2d_list(self.matrix2, "Second matrix")
                        self.print_2d_list(result, "Product matrix")
                elif choice in [2, 3]:
                    rows = input("Enter number of rows: ")
                    cols = input("Enter number of columns: ")
                    self.matrix1 = self.create_2d_list(rows, cols, "Enter numbers for matrix")
                    if not self.matrix1:
                        continue
                    if choice == 2:
                        result = self.extract_border_elements(self.matrix1)
                        self.print_2d_list(self.matrix1, "Matrix")
                        print(f"Border elements (clockwise): {result}")
                    elif choice == 3:
                        max_val, max_pos = self.find_max_element(self.matrix1)
                        self.print_2d_list(self.matrix1, "Matrix")
                        if max_val is None:
                            print("No maximum element found.")
                        else:
                            print(f"Maximum element: {max_val} at position {max_pos}")
                elif choice == 4:
                    self.print_2d_list(self.matrix1, "Current Matrix 1")
                    self.print_2d_list(self.matrix2, "Current Matrix 2")
            except ValueError:
                print("Invalid input. Please enter a valid number for choice.")

if __name__ == "__main__":
    solver = MatrixChallengeSolver()
    solver.run()