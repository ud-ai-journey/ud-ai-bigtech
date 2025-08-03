# 🔧 Day 10: Basic Functions - Code Architecture Fundamentals
# Learning: Function definition, calling, and basic structure

print("🔧 Basic Functions - The Code Factories")
print("=" * 50)

# 1. Simple Function - No parameters, no return
def greet_user():
    """A simple greeting function - like a friendly receptionist"""
    print("Hello! Welcome to the world of functions! 🌟")
    print("Functions are like mini-factories that do specific jobs.")

# 2. Function with Parameters - Input processing
def greet_person(name):
    """Personalized greeting - like a smart receptionist who remembers names"""
    print(f"Hello {name}! Great to see you learning functions! 🚀")

# 3. Function with Multiple Parameters
def calculate_rectangle_area(length, width):
    """Calculate area - like a blueprint calculator"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {area} square units")

# 4. Function with Return Value - The Result Producer
def add_numbers(a, b):
    """Addition function - returns the result instead of just printing"""
    result = a + b
    return result

# 5. Function with Default Parameters - Smart Defaults
def introduce_person(name, age=18, city="Unknown"):
    """Introduction with default values - like a form with pre-filled fields"""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print()

# 6. Pattern Function - Converting our pattern skills into reusable code!
def print_star_line(num_stars):
    """Print a line of stars - building block for patterns"""
    for i in range(num_stars):
        print("*", end=" ")
    print()  # New line after stars

# 7. Advanced Pattern Function - Right Triangle using Function
def draw_right_triangle(rows):
    """Draw right triangle using our reusable star function"""
    print(f"🎨 Right Triangle with {rows} rows:")
    for i in range(1, rows + 1):
        print_star_line(i)
    print()

# TESTING OUR FUNCTIONS - The Function Playground!
print("\n🎪 FUNCTION DEMONSTRATIONS:")
print("-" * 40)

# Test basic functions
print("1. Basic Greeting:")
greet_user()
print()

print("2. Personalized Greeting:")
greet_person("Uday Kumar")
print()

print("3. Rectangle Area Calculator:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)
print()

print("4. Addition with Return Value:")
sum1 = add_numbers(15, 25)
sum2 = add_numbers(100, 200)
print(f"15 + 25 = {sum1}")
print(f"100 + 200 = {sum2}")
print()

print("5. Introduction with Default Parameters:")
introduce_person("Alice")  # Uses default age and city
introduce_person("Bob", 25)  # Uses default city only
introduce_person("Charlie", 30, "New York")  # All custom values

print("6. Pattern Functions in Action:")
draw_right_triangle(5)
draw_right_triangle(3)

print("🎉 Functions make code reusable, organized, and powerful!")
print("You've just become a Code Architect! 🏗️")