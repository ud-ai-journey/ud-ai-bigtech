class MatrixChallengeSolver:
    def __init__(self):
        """Initialize empty matrix for storing inputs."""
        self.matrix = []

    def create_2d_list(self, rows, cols):
        """Create a 2D list with user-input values."""
        try:
            rows, cols = int(rows), int(cols)
            if rows < 1 or cols < 1:
                print("Rows and columns must be positive.")
                return []
            print(f"Enter {rows * cols} numbers for a {rows}x{cols} matrix (row-wise, comma-separated):")
            values = input().split(",")
            if len(values) != rows * cols:
                print(f"Expected {rows * cols} numbers, got {len(values)}.")
                return []
            return [[int(values[i * cols + j]) for j in range(cols)] for i in range(rows)]
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            return []

    def print_1d_list(self, lst, message="Result"):
        """Print a 1D list with a custom message."""
        if not lst:
            print("List is empty.")
        else:
            print(f"{message}: {lst}")

    def print_2d_list(self, matrix, message="Matrix"):
        """Print a 2D list in a readable format."""
        if not matrix:
            print("Matrix is empty.")
        else:
            print(message + ":")
            for row in matrix:
                print(" ".join(map(str, row)))

    def matrix_spiral_traversal(self, matrix):
        """Traverse a matrix in spiral order and return elements as a 1D list."""
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])
        result = []
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
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

    def flip_matrix_horizontally(self, matrix):
        """Flip a matrix horizontally by reversing each row in-place."""
        if not matrix:
            return
        for row in matrix:
            row.reverse()

    def count_element_occurrences(self, matrix, target):
        """Count occurrences of a target element in a matrix."""
        if not matrix or not matrix[0]:
            return 0
        return sum(row.count(target) for row in matrix)

    def display_menu(self):
        """Display the interactive menu."""
        print("\nMatrix Challenge Solver Menu:")
        print("1. Matrix Spiral Traversal")
        print("2. Flip Matrix Horizontally")
        print("3. Count Element Occurrences")
        print("4. Print Current Matrix")
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
                if choice in [1, 2, 3]:
                    rows = input("Enter number of rows: ")
                    cols = input("Enter number of columns: ")
                    self.matrix = self.create_2d_list(rows, cols)
                    if not self.matrix:
                        continue
                if choice == 1:
                    result = self.matrix_spiral_traversal(self.matrix)
                    self.print_2d_list(self.matrix, "Matrix")
                    self.print_1d_list(result, "Spiral traversal")
                elif choice == 2:
                    self.print_2d_list(self.matrix, "Original matrix")
                    self.flip_matrix_horizontally(self.matrix)
                    self.print_2d_list(self.matrix, "Horizontally flipped matrix")
                elif choice == 3:
                    target = input("Enter target value to count: ")
                    try:
                        target = int(target)
                        self.print_2d_list(self.matrix, "Matrix")
                        count = self.count_element_occurrences(self.matrix, target)
                        print(f"Occurrences of {target}: {count}")
                    except ValueError:
                        print("Invalid target. Please enter a number.")
                elif choice == 4:
                    self.print_2d_list(self.matrix, "Current Matrix")
            except ValueError:
                print("Invalid input. Please enter a valid number for choice.")

if __name__ == "__main__":
    solver = MatrixChallengeSolver()
    solver.run()