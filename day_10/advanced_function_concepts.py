# 🚀 Day 10: Advanced Function Concepts - The Professional Toolkit
# Learning: Lambda functions, higher-order functions, decorators, and challenges

print("🚀 Advanced Function Concepts - Professional Developer Toolkit")
print("=" * 65)

# LAMBDA FUNCTIONS - The Quick Helpers
print("1. LAMBDA FUNCTIONS - The One-Line Wonders:")
print("-" * 45)

# Regular function vs Lambda comparison
def square_regular(x):
    return x * x

square_lambda = lambda x: x * x

# Multiple lambda examples
add = lambda a, b: a + b
is_even = lambda n: n % 2 == 0
get_length = lambda s: len(s)
max_of_two = lambda a, b: a if a > b else b

print("Regular function vs Lambda:")
print(f"square_regular(5) = {square_regular(5)}")
print(f"square_lambda(5) = {square_lambda(5)}")
print()

print("Lambda function examples:")
print(f"add(10, 20) = {add(10, 20)}")
print(f"is_even(7) = {is_even(7)}")
print(f"get_length('Python') = {get_length('Python')}")
print(f"max_of_two(15, 8) = {max_of_two(15, 8)}")
print()

# HIGHER-ORDER FUNCTIONS - Functions that work with other functions
print("2. HIGHER-ORDER FUNCTIONS - Functions Using Functions:")
print("-" * 55)

def apply_operation(numbers, operation):
    """Apply an operation to all numbers in a list"""
    result = []
    for num in numbers:
        result.append(operation(num))
    return result

def filter_numbers(numbers, condition):
    """Filter numbers based on a condition function"""
    result = []
    for num in numbers:
        if condition(num):
            result.append(num)
    return result

def calculate_with_operation(a, b, operation):
    """Perform calculation using provided operation function"""
    return operation(a, b)

# Testing higher-order functions
test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original numbers:", test_numbers)
squared = apply_operation(test_numbers, square_lambda)
print("Squared:", squared)

doubled = apply_operation(test_numbers, lambda x: x * 2)
print("Doubled:", doubled)

even_numbers = filter_numbers(test_numbers, is_even)
print("Even numbers:", even_numbers)

big_numbers = filter_numbers(test_numbers, lambda x: x > 5)
print("Numbers > 5:", big_numbers)

print(f"Calculate 15 + 25 = {calculate_with_operation(15, 25, add)}")
print(f"Calculate 15 * 25 = {calculate_with_operation(15, 25, lambda x, y: x * y)}")
print()

# FUNCTION DECORATORS - Functions that enhance other functions
print("3. FUNCTION DECORATORS - Function Enhancers:")
print("-" * 45)

def timer_decorator(func):
    """Decorator to measure function execution time"""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏱️ {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def logger_decorator(func):
    """Decorator to log function calls"""
    def wrapper(*args, **kwargs):
        print(f"📝 Calling {func.__name__} with args: {args}")
        result = func(*args, **kwargs)
        print(f"📝 {func.__name__} returned: {result}")
        return result
    return wrapper

# Using decorators
@timer_decorator
def slow_calculation(n):
    """A function that takes some time"""
    total = 0
    for i in range(n):
        total += i * i
    return total

@logger_decorator
def add_three_numbers(a, b, c):
    """Add three numbers together"""
    return a + b + c

print("Testing decorated functions:")
result = slow_calculation(100000)
print(f"Calculation result: {result}")
print()

sum_result = add_three_numbers(10, 20, 30)
print()

# RECURSIVE FUNCTIONS - Functions that call themselves
print("4. RECURSIVE FUNCTIONS - Self-Calling Functions:")
print("-" * 50)

def factorial(n):
    """Calculate factorial using recursion"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Calculate Fibonacci number using recursion"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def draw_recursive_triangle(rows, current_row=1):
    """Draw triangle using recursion"""
    if current_row > rows:
        return
    
    # Print current row
    print("* " * current_row)
    # Recursive call for next row
    draw_recursive_triangle(rows, current_row + 1)

print("Factorial examples:")
for i in range(1, 6):
    print(f"{i}! = {factorial(i)}")
print()

print("Fibonacci sequence:")
for i in range(8):
    print(f"F({i}) = {fibonacci(i)}")
print()

print("Recursive triangle:")
draw_recursive_triangle(5)
print()

# FUNCTION CHALLENGES - Interview-Style Problems
print("5. FUNCTION CHALLENGES - Interview Practice:")
print("-" * 45)

def find_prime_numbers(limit):
    """Find all prime numbers up to a given limit"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def analyze_text(text):
    """Analyze text and return statistics"""
    words = text.split()
    
    def count_vowels(word):
        vowels = 'aeiouAEIOU'
        return sum(1 for char in word if char in vowels)
    
    analysis = {
        'total_words': len(words),
        'total_chars': len(text),
        'average_word_length': sum(len(word) for word in words) / len(words) if words else 0,
        'longest_word': max(words, key=len) if words else '',
        'total_vowels': sum(count_vowels(word) for word in words)
    }
    
    return analysis

def create_calculator():
    """Create a calculator using nested functions"""
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        return a / b if b != 0 else "Cannot divide by zero"
    
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    def calculate(a, operator, b):
        if operator in operations:
            return operations[operator](a, b)
        else:
            return "Invalid operator"
    
    return calculate

# Testing challenges
print("Prime numbers up to 20:")
primes = find_prime_numbers(20)
print(primes)
print()

sample_text = "Python is an amazing programming language for beginners and experts"
text_stats = analyze_text(sample_text)
print("Text Analysis:")
print(f"Text: '{sample_text}'")
for key, value in text_stats.items():
    print(f"  {key}: {value}")
print()

calculator = create_calculator()
print("Calculator tests:")
print(f"10 + 5 = {calculator(10, '+', 5)}")
print(f"20 - 8 = {calculator(20, '-', 8)}")
print(f"6 * 7 = {calculator(6, '*', 7)}")
print(f"15 / 3 = {calculator(15, '/', 3)}")
print(f"10 / 0 = {calculator(10, '/', 0)}")
print()

# FUNCTION BEST PRACTICES
print("🎯 ADVANCED FUNCTION BEST PRACTICES:")
print("-" * 40)
print("✅ Lambda: Use for simple, one-line functions")
print("✅ Higher-order: Functions can take and return other functions")
print("✅ Decorators: Add functionality without modifying original function")
print("✅ Recursion: Elegant for problems with repeated subproblems")
print("✅ Nested functions: Organize related functionality together")
print("✅ Pure functions: Same input always gives same output")
print("✅ Function composition: Combine simple functions to build complex ones")
print()

print("🎉 You've mastered advanced function concepts!")
print("You're now ready for professional Python development! 🐍👨‍💻")