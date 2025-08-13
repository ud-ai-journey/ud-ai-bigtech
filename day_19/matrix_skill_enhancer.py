class MatrixSkillEnhancer:
    def __init__(self):
        """Initialize empty matrices for storing inputs."""
        self.matrix_1 = []
        self.matrix_2 = []

    def create_2d_list(self, rows, cols, prompt="matrix"):
        """Create a 2D list with user-input values."""
        try:
            rows, cols = int(rows), int(cols)
            if rows < 1 or cols < 1:
                print("Rows and columns must be positive.")
                return []
            print(f"Enter {rows * cols} numbers for a {rows}x{cols} {prompt} (row-wise, comma-separated):")
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
            print("Matrix dimensions incompatible for multiplication.")
            return []
        result = [[0 for _ in range(cols2)] for _ in range(rows1)]
        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        return result

    def row_maximum_elements(self, matrix):
        """Find the maximum element in each row of a matrix."""
        if not matrix:
            return []
        return [max(row) for row in matrix]

    def is_symmetric_matrix(self, matrix):
        """Check if a square matrix is symmetric (equal to its transpose)."""
        if not matrix or not matrix[0]:
            return False
        n = len(matrix)
        if any(len(row) != n for row in matrix):
            return False
        for i in range(n):
            for j in range(i, n):
                if matrix[i][j] != matrix[j][i]:
                    return False
        return True

    def display_menu(self):
        """Display the interactive menu."""
        print("\nMatrix Skill Enhancer Menu:")
        print("1. Matrix Multiplication")
        print("2. Row Maximum Elements")
        print("3. Check Symmetric Matrix")
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
                    self.matrix_1 = self.create_2d_list(rows1, cols1, "first matrix")
                    if not self.matrix_1:
                        continue
                    rows2 = input("Enter number of rows for second matrix: ")
                    cols2 = input("Enter number of columns for second matrix: ")
                    self.matrix_2 = self.create_2d_list(rows2, cols2, "second matrix")
                    if not self.matrix_2:
                        continue
                    result = self.matrix_multiplication(self.matrix_1, self.matrix_2)
                    if result:
                        self.print_2d_list(self.matrix_1, "First matrix")
                        self.print_2d_list(self.matrix_2, "Second matrix")
                        self.print_2d_list(result, "Product matrix")
                elif choice == 2:
                    rows = input("Enter number of rows: ")
                    cols = input("Enter number of columns: ")
                    self.matrix_1 = self.create_2d_list(rows, cols)
                    if self.matrix_1:
                        result = self.row_maximum_elements(self.matrix_1)
                        self.print_2d_list(self.matrix_1, "Matrix")
                        print(f"Row maximums: {result}")
                elif choice == 3:
                    rows = input("Enter size of square matrix: ")
                    self.matrix_1 = self.create_2d_list(rows, rows)
                    if self.matrix_1:
                        result = self.is_symmetric_matrix(self.matrix_1)
                        self.print_2d_list(self.matrix_1, "Matrix")
                        print(f"Matrix is {'symmetric' if result else 'not symmetric'}.")
                elif choice == 4:
                    self.print_2d_list(self.matrix_1, "Current Matrix 1")
                    self.print_2d_list(self.matrix_2, "Current Matrix 2")
            except ValueError:
                print("Invalid input. Please enter a valid number for choice.")

if __name__ == "__main__":
    solver = MatrixSkillEnhancer()
    solver.run()