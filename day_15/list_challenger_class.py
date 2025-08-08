class ListChallengeSolver:
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

    def create_2d_list(self, size):
        """Create a square 2D list with user-input values."""
        try:
            size = int(size)
            if size < 1:
                print("Size must be positive.")
                return []
            print(f"Enter {size * size} numbers for a {size}x{size} matrix (row-wise, comma-separated):")
            values = input().split(",")
            if len(values) != size * size:
                print(f"Expected {size * size} numbers, got {len(values)}.")
                return []
            return [[int(values[i * size + j]) for j in range(size)] for i in range(size)]
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

    def filter_even_numbers(self, lst):
        """Filter out even numbers, returning a list of odd numbers."""
        return [x for x in lst if x % 2 != 0]

    def rotate_matrix_90(self, matrix):
        """Rotate a square matrix 90 degrees clockwise in-place."""
        if not matrix:
            return
        n = len(matrix)
        # Transpose (swap elements across diagonal)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for i in range(n):
            matrix[i].reverse()

    def flatten_2d_list(self, matrix):
        """Flatten a 2D list into a 1D list in row-major order."""
        if not matrix:
            return []
        return [element for row in matrix for element in row]

    def display_menu(self):
        """Display the interactive menu."""
        print("\nList Challenge Solver Menu:")
        print("1. Filter Even Numbers from 1D List")
        print("2. Rotate Matrix 90 Degrees")
        print("3. Flatten 2D List")
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
                    self.list_1 = self.create_1d_list("Enter numbers for 1D list (e.g., 1,2,3,4): ")
                    if self.list_1:
                        result = self.filter_even_numbers(self.list_1)
                        self.print_1d_list(result, "Odd numbers")
                elif choice == 2:
                    size = input("Enter size of square matrix: ")
                    self.matrix = self.create_2d_list(size)
                    if self.matrix:
                        self.print_2d_list(self.matrix, "Original matrix")
                        self.rotate_matrix_90(self.matrix)
                        self.print_2d_list(self.matrix, "Rotated matrix")
                elif choice == 3:
                    size = input("Enter size of square matrix: ")
                    self.matrix = self.create_2d_list(size)
                    if self.matrix:
                        result = self.flatten_2d_list(self.matrix)
                        self.print_1d_list(result, "Flattened list")
                elif choice == 4:
                    self.print_1d_list(self.list_1, "Current 1D List")
                    self.print_2d_list(self.matrix, "Current 2D List")
            except ValueError:
                print("Invalid input. Please enter a valid number for choice.")

if __name__ == "__main__":
    solver = ListChallengeSolver()
    solver.run()