class ListSkillBuilder:
    def __init__(self):
        """Initialize empty lists for storing inputs."""
        self.list_1 = []
        self.list_2 = []
        self.matrix = []

    def create_1d_list(self, prompt):
        """Create a 1D list from a comma-separated string of numbers."""
        try:
            elements = input(prompt)
            lst = [int(x) for x in elements.split(",")]
            # Ensure sorted for merge problem
            if "sorted" in prompt.lower():
                lst = sorted(lst)
            return lst
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

    def matrix_diagonal_traversal(self, matrix):
        """Traverse the main diagonal of a matrix and return elements."""
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])
        n = min(rows, cols)
        return [matrix[i][i] for i in range(n)]

    def merge_sorted_lists(self, list1, list2):
        """Merge two sorted lists into a single sorted list."""
        result = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        result.extend(list1[i:])
        result.extend(list2[j:])
        return result

    def find_second_largest(self, lst):
        """Find the second largest element in a 1D list."""
        if len(lst) < 2:
            return None
        first = second = float('-inf')
        for num in lst:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num
        return second if second != float('-inf') else None

    def display_menu(self):
        """Display the interactive menu."""
        print("\nList Skill Builder Menu:")
        print("1. Matrix Diagonal Traversal")
        print("2. Merge Two Sorted Lists")
        print("3. Find Second Largest Element")
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
                        result = self.matrix_diagonal_traversal(self.matrix)
                        self.print_2d_list(self.matrix, "Matrix")
                        self.print_1d_list(result, "Diagonal elements")
                elif choice == 2:
                    self.list_1 = self.create_1d_list("Enter numbers for first sorted list (e.g., 1,3,5): ")
                    self.list_2 = self.create_1d_list("Enter numbers for second sorted list (e.g., 2,4,6): ")
                    if self.list_1 and self.list_2:
                        result = self.merge_sorted_lists(self.list_1, self.list_2)
                        self.print_1d_list(self.list_1, "First list")
                        self.print_1d_list(self.list_2, "Second list")
                        self.print_1d_list(result, "Merged sorted list")
                elif choice == 3:
                    self.list_1 = self.create_1d_list("Enter numbers for 1D list (e.g., 1,2,3,4): ")
                    if self.list_1:
                        result = self.find_second_largest(self.list_1)
                        self.print_1d_list(self.list_1, "List")
                        if result is None:
                            print("No second largest element exists.")
                        else:
                            print(f"Second largest element: {result}")
                elif choice == 4:
                    self.print_1d_list(self.list_1, "Current 1D List 1")
                    self.print_1d_list(self.list_2, "Current 1D List 2")
                    self.print_2d_list(self.matrix, "Current 2D List")
            except ValueError:
                print("Invalid input. Please enter a valid number for choice.")

if __name__ == "__main__":
    solver = ListSkillBuilder()
    solver.run()