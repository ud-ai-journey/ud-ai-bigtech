def number_pyramid(rows):
    """Prints a pyramid of numbers increasing and decreasing."""
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

def alphabetical_diamond(rows):
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

def spiral_pattern(size):
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

def pascal_triangle(rows):
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

def fibonacci_square(size):
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

def star_hourglass(rows):
    """Prints an hourglass pattern using stars."""
    n = (rows + 1) // 2
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1))
    for i in range(2, n + 1):
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1))

def prime_number_triangle(rows):
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

def checkerboard_pattern(size):
    """Prints a checkerboard pattern using 0s and 1s."""
    for i in range(size):
        for j in range(size):
            print((i + j) % 2, end=" ")
        print()

def diagonal_wave(rows):
    """Prints a diagonal wave pattern using slashes."""
    for i in range(rows):
        print(" " * i + "\\" + " " * (2 * (rows - i - 1)) + "/")
    for i in range(rows - 2, -1, -1):
        print(" " * i + "\\" + " " * (2 * (rows - i - 1)) + "/")

def main():
    print("Number Pyramid (5 rows):")
    number_pyramid(5)
    print("\nAlphabetical Diamond (7 rows):")
    alphabetical_diamond(7)
    print("\nSpiral Pattern (5x5):")
    spiral_pattern(5)
    print("\nPascal's Triangle (6 rows):")
    pascal_triangle(6)
    print("\nFibonacci Square (4x4):")
    fibonacci_square(4)
    print("\nStar Hourglass (7 rows):")
    star_hourglass(7)
    print("\nPrime Number Triangle (5 rows):")
    prime_number_triangle(5)
    print("\nCheckerboard Pattern (5x5):")
    checkerboard_pattern(5)
    print("\nDiagonal Wave (4 rows):")
    diagonal_wave(4)

if __name__ == "__main__":
    main()