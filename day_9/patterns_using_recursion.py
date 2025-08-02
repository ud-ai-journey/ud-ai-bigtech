class PatternGenerator:
    def __init__(self):
        pass  # No initialization needed

    # Pattern methods
    def number_pyramid(self, rows):
        """Prints a pyramid of numbers increasing and decreasing."""
        for i in range(1, rows + 1):
            print(" " * (rows - i), end="")
            for j in range(1, i + 1):
                print(j, end="")
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()

    def alphabetical_diamond(self, rows):
        """Prints a diamond pattern using alphabets."""
        n = (rows + 1) // 2
        for i in range(1, n + 1):
            print(" " * (n - i), end="")
            for j in range(1, i + 1):
                print(chr(64 + j), end=" ")
            print()
        for i in range(n - 1, 0, -1):
            print(" " * (n - i), end="")
            for j in range(1, i + 1):
                print(chr(64 + j), end=" ")
            print()

    def spiral_pattern(self, size):
        """Prints a spiral pattern in a square matrix."""
        if size % 2 == 0:
            size += 1
        matrix = [[0] * size for _ in range(size)]
        top, bottom, left, right = 0, size - 1, 0, size - 1
        num = 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        for row in matrix:
            for num in row:
                print(f"{num:3}", end=" ")
            print()

    def pascal_triangle(self, rows):
        """Prints Pascal's Triangle."""
        triangle = [[1]]
        for i in range(1, rows):
            prev_row = triangle[-1]
            new_row = [1]
            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])
            new_row.append(1)
            triangle.append(new_row)
        max_width = len(" ".join(map(str, triangle[-1])))
        for row in triangle:
            row_str = " ".join(map(str, row))
            print(row_str.center(max_width))

    def fibonacci_square(self, size):
        """Prints a square pattern with Fibonacci numbers."""
        fib = [1, 1]
        for i in range(2, size * size):
            fib.append(fib[i-1] + fib[i-2])
        matrix = [[0] * size for _ in range(size)]
        index = 0
        for i in range(size):
            for j in range(size):
                matrix[i][j] = fib[index]
                index += 1
        for row in matrix:
            for num in row:
                print(f"{num:4}", end=" ")
            print()

    def star_hourglass(self, rows):
        """Prints an hourglass pattern using stars."""
        n = (rows + 1) // 2
        for i in range(n, 0, -1):
            print(" " * (n - i), end="")
            print("*" * (2 * i - 1))
        for i in range(2, n + 1):
            print(" " * (n - i), end="")
            print("*" * (2 * i - 1))

    def prime_number_triangle(self, rows):
        """Prints a triangle with prime numbers."""
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        primes = [n for n in range(2, 100) if is_prime(n)]
        index = 0
        for i in range(1, rows + 1):
            print(" " * (rows - i), end="")
            for j in range(i):
                if index < len(primes):
                    print(f"{primes[index]:2}", end=" ")
                    index += 1
            print()

    def checkerboard_pattern(self, size):
        """Prints a checkerboard pattern using 0s and 1s."""
        for i in range(size):
            for j in range(size):
                print((i + j) % 2, end=" ")
            print()

    def diagonal_wave(self, rows):
        """Prints a diagonal wave pattern using slashes."""
        for i in range(rows):
            print(" " * i + "\\" + " " * (2 * (rows - i - 1)) + "/")
        for i in range(rows - 2, -1, -1):
            print(" " * i + "\\" + " " * (2 * (rows - i - 1)) + "/")

    def hollow_square(self, size):
        """Prints a hollow square pattern with stars on the border."""
        if size < 2:
            print("Size must be at least 2")
            return
        print("*" * size)
        for i in range(size - 2):
            print("*" + " " * (size - 2) + "*")
        print("*" * size)

    # Helper methods for grid patterns
    def _create_checkerboard(self, rows, cols):
        """Creates a 2D list representing a checkerboard pattern."""
        return [[(i + j) % 2 for j in range(cols)] for i in range(rows)]

    def _print_grid(self, grid):
        """Prints a 2D grid in a readable format."""
        for row in grid:
            print(" ".join(map(str, row)))

    def _rotate_grid(self, grid):
        """Rotates a 2D grid 90 degrees clockwise."""
        return [list(row) for row in zip(*grid[::-1])]

    def _mirror_grid(self, grid):
        """Mirrors a 2D grid horizontally (left-right flip)."""
        return [row[::-1] for row in grid]

    def grid_checkerboard_pattern(self, rows, cols):
        """Prints a checkerboard pattern using a 2D grid."""
        grid = self._create_checkerboard(rows, cols)
        self._print_grid(grid)

    def rotated_checkerboard_pattern(self, rows, cols):
        """Prints a checkerboard pattern rotated 90 degrees clockwise."""
        grid = self._create_checkerboard(rows, cols)
        rotated = self._rotate_grid(grid)
        self._print_grid(rotated)

    def mirrored_checkerboard_pattern(self, rows, cols):
        """Prints a checkerboard pattern mirrored horizontally."""
        grid = self._create_checkerboard(rows, cols)
        mirrored = self._mirror_grid(grid)
        self._print_grid(mirrored)

    # Fibonacci sequence methods
    def _generate_fibonacci(self, n):
        """Recursively generates the first n Fibonacci numbers."""
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib_n_minus_1 = self._generate_fibonacci(n - 1)
            next_fib = fib_n_minus_1[-1] + fib_n_minus_1[-2]
            return fib_n_minus_1 + [next_fib]

    def fibonacci_pattern(self, n):
        """Prints the first n Fibonacci numbers."""
        if n < 1:
            print("Number of terms must be at least 1")
            return
        sequence = self._generate_fibonacci(n)
        print(f"Fibonacci Sequence (first {n} terms):")
        for num in sequence:
            print(num)

    # Menu and run methods
    def display_menu(self):
        """Displays the pattern selection menu."""
        print("\nAvailable Patterns:")
        print("1. Number Pyramid")
        print("2. Alphabetical Diamond")
        print("3. Spiral Pattern")
        print("4. Pascal's Triangle")
        print("5. Fibonacci Square")
        print("6. Star Hourglass")
        print("7. Prime Number Triangle")
        print("8. Checkerboard Pattern")
        print("9. Diagonal Wave")
        print("10. Hollow Square")
        print("11. Grid Checkerboard")
        print("12. Rotated Checkerboard")
        print("13. Mirrored Checkerboard")
        print("14. Fibonacci Sequence")
        print("0. Exit")

    def run(self):
        """Runs the interactive menu and handles user input."""
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice (0-14): "))
                if choice == 0:
                    print("Exiting...")
                    break
                if choice not in range(1, 15):
                    print("Invalid choice. Please select 0-14.")
                    continue
                if choice in [11, 12, 13]:
                    rows = int(input("Enter the number of rows (2-10): "))
                    cols = int(input("Enter the number of columns (2-10): "))
                    if rows < 2 or rows > 10 or cols < 2 or cols > 10:
                        print("Rows and columns must be between 2 and 10.")
                        continue
                elif choice == 14:
                    n = int(input("Enter the number of terms (1-20): "))
                    if n < 1 or n > 20:
                        print("Number of terms must be between 1 and 20.")
                        continue
                else:
                    size = int(input("Enter the number of rows/size (2-10): "))
                    if size < 2 or size > 10:
                        print("Size must be between 2 and 10.")
                        continue
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            print(f"\nPattern {choice}:")
            if choice == 1:
                self.number_pyramid(size)
            elif choice == 2:
                self.alphabetical_diamond(size)
            elif choice == 3:
                self.spiral_pattern(size)
            elif choice == 4:
                self.pascal_triangle(size)
            elif choice == 5:
                self.fibonacci_square(size)
            elif choice == 6:
                self.star_hourglass(size)
            elif choice == 7:
                self.prime_number_triangle(size)
            elif choice == 8:
                self.checkerboard_pattern(size)
            elif choice == 9:
                self.diagonal_wave(size)
            elif choice == 10:
                self.hollow_square(size)
            elif choice == 11:
                self.grid_checkerboard_pattern(rows, cols)
            elif choice == 12:
                self.rotated_checkerboard_pattern(rows, cols)
            elif choice == 13:
                self.mirrored_checkerboard_pattern(rows, cols)
            elif choice == 14:
                self.fibonacci_pattern(n)

if __name__ == "__main__":
    generator = PatternGenerator()
    generator.run()