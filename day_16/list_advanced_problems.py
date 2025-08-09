class ListAdvancedSolver:
    def __init__(self):
        """Initialize empty lists for storing inputs."""
        self.list_1 = []
        self.matrix = []

    def create_1d_list(self, prompt):
        """Create a 1D list from a comma-separated string of numbers."""
        try:
            elements = input(prompt)
            return [int(x) for x in elements.split(",")]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            return []

    def create_2d_list(self, rows, cols):
        """Create a 2D list with user-input values, sorted rows and columns."""
        try:
            rows, cols = int(rows), int(cols)
            if rows < 1 or cols < 1:
                print("Rows and columns must be positive.")
                return []
            print(f"Enter {rows * cols} numbers for a {rows}x{cols} matrix (row-wise, sorted rows):")
            values = input().split(",")
            if len(values) != rows * cols:
                print(f"Expected {rows * cols} numbers, got {len(values)}.")
                return []
            matrix = [[int(values[i * cols + j]) for j in range(cols)] for i in range(rows)]
            # Verify each row is sorted
            for row in matrix:
                if row != sorted(row):
                    print("Each row must be sorted in ascending order.")
                    return []
            # Verify each column is sorted
            for j in range(cols):
                column = [matrix[i][j] for i in range(rows)]
                if column != sorted(column):
                    print("Each column must be sorted in ascending order.")
                    return []
            return matrix
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

    def search_sorted_matrix(self, matrix, target):
        """Search for a target in a sorted matrix, return coordinates or (-1, -1)."""
        if not matrix or not matrix[0]:
            return (-1, -1)
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1  # Start from top-right corner
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return (row, col)
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return (-1, -1)

    def reverse_list_inplace(self, lst):
        """Reverse a 1D list in-place."""
        left, right = 0, len(lst) - 1
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        return lst

    def max_subarray_sum(self, lst):
        """Find the maximum subarray sum using Kadane's algorithm."""
        if not lst:
            return 0
        max_so_far = max_ending_here = lst[0]
        for num in lst[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    def display_menu(self):
        """Display the interactive menu."""
        print("\nList Advanced Solver Menu:")
        print("1. Search in Sorted Matrix")
        print("2. Reverse List In-Place")
        print("3. Find Maximum Subarray Sum")
        print("4. Print Current Lists")
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
                    rows = input("Enter number of rows: ")
                    cols = input("Enter number of columns: ")
                    self.matrix = self.create_2d_list(rows, cols)
                    if self.matrix:
                        target = input("Enter target value to search: ")
                        try:
                            target = int(target)
                            result = self.search_sorted_matrix(self.matrix, target)
                            if result == (-1, -1):
                                print(f"Target {target} not found in matrix.")
                            else:
                                print(f"Target {target} found at coordinates {result}.")
                            self.print_2d_list(self.matrix, "Matrix")
                        except ValueError:
                            print("Invalid target. Please enter a number.")
                elif choice == 2:
                    self.list_1 = self.create_1d_list("Enter numbers for 1D list (e.g., 1,2,3,4): ")
                    if self.list_1:
                        self.print_1d_list(self.list_1, "Original list")
                        result = self.reverse_list_inplace(self.list_1)
                        self.print_1d_list(result, "Reversed list")
                elif choice == 3:
                    self.list_1 = self.create_1d_list("Enter numbers for 1D list (e.g., -2,1,-3,4): ")
                    if self.list_1:
                        result = self.max_subarray_sum(self.list_1)
                        self.print_1d_list(self.list_1, "List")
                        print(f"Maximum subarray sum: {result}")
                elif choice == 4:
                    self.print_1d_list(self.list_1, "Current 1D List")
                    self.print_2d_list(self.matrix, "Current 2D List")
            except ValueError:
                print("Invalid input. Please enter a valid number for choice.")

if __name__ == "__main__":
    solver = ListAdvancedSolver()
    solver.run()