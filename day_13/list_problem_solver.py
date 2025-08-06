class ListProblemSolver:
    def __init__(self):
        """Initialize empty lists for storing inputs."""
        self.list_1 = []
        self.list_2 = []
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

    def remove_duplicates(self, lst):
        """Remove duplicates from a 1D list, preserving order."""
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    def matrix_row_sum(self, matrix):
        """Compute the sum of each row in a 2D list."""
        if not matrix:
            return []
        return [sum(row) for row in matrix]

    def find_common_elements(self, list1, list2):
        """Find common elements between two 1D lists, sorted in ascending order."""
        common = [x for x in set(list1) if x in list2]
        return sorted(common)

    def display_menu(self):
        """Display the interactive menu."""
        print("\nList Problem Solver Menu:")
        print("1. Remove Duplicates from 1D List")
        print("2. Compute Matrix Row Sums")
        print("3. Find Common Elements in Two Lists")
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
                    self.list_1 = self.create_1d_list("Enter numbers for 1D list (e.g., 1,2,2,3): ")
                    if self.list_1:
                        result = self.remove_duplicates(self.list_1)
                        self.print_1d_list(result, "List with duplicates removed")
                elif choice == 2:
                    rows = input("Enter number of rows: ")
                    cols = input("Enter number of columns: ")
                    self.matrix = self.create_2d_list(rows, cols)
                    if self.matrix:
                        result = self.matrix_row_sum(self.matrix)
                        self.print_1d_list(result, "Row sums")
                elif choice == 3:
                    self.list_1 = self.create_1d_list("Enter numbers for first list (e.g., 1,2,3): ")
                    self.list_2 = self.create_1d_list("Enter numbers for second list (e.g., 2,3,4): ")
                    if self.list_1 and self.list_2:
                        result = self.find_common_elements(self.list_1, self.list_2)
                        self.print_1d_list(result, "Common elements")
                elif choice == 4:
                    self.print_1d_list(self.list_1, "Current 1D List 1")
                    self.print_1d_list(self.list_2, "Current 1D List 2")
                    self.print_2d_list(self.matrix, "Current 2D List")
            except ValueError:
                print("Invalid input. Please enter a valid number for choice.")

if __name__ == "__main__":
    solver = ListProblemSolver()
    solver.run()