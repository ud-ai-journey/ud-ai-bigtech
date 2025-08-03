# 🎯 Day 10: Return Values & Types - The Function Output Masters
# Learning: Different types of return values and how to use them

print("🎯 Return Values & Types - Functions That Give Back")
print("=" * 55)

# 1. Functions returning different data types
def get_user_info():
    """Function that returns multiple pieces of information"""
    name = "Uday Kumar"
    age = 22
    is_student = True
    return name, age, is_student  # Returns a tuple

def calculate_circle_properties(radius):
    """Function returning multiple calculated values"""
    import math
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return area, circumference, diameter

def is_even(number):
    """Function returning boolean - True/False"""
    return number % 2 == 0

def get_grade(score):
    """Function returning string based on conditions"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def find_max_in_list(numbers):
    """Function returning the maximum number from a list"""
    if not numbers:  # Empty list check
        return None
    
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def create_pattern_info(rows):
    """Function returning information about a pattern"""
    total_stars = 0
    for i in range(1, rows + 1):
        total_stars += i
    
    pattern_type = "Right Triangle"
    pattern_description = f"{pattern_type} with {rows} rows using {total_stars} total stars"
    
    return {
        "type": pattern_type,
        "rows": rows,
        "total_stars": total_stars,
        "description": pattern_description
    }

# 2. Functions with conditional returns
def check_number_type(num):
    """Function with multiple return paths"""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def validate_age(age):
    """Function with validation and different return types"""
    if age < 0:
        return False, "Invalid age: cannot be negative"
    elif age < 18:
        return True, "Minor"
    elif age < 65:
        return True, "Adult"
    else:
        return True, "Senior"

# 3. Pattern functions that return data instead of just printing
def generate_star_line(num_stars):
    """Generate a line of stars as a string"""
    return "* " * num_stars

def create_triangle_pattern(rows):
    """Create triangle pattern and return as list of strings"""
    pattern_lines = []
    for i in range(1, rows + 1):
        line = "* " * i
        pattern_lines.append(line)
    return pattern_lines

# TESTING ALL RETURN TYPES - The Return Value Laboratory!
print("\n🧪 RETURN VALUE EXPERIMENTS:")
print("-" * 40)

print("1. Multiple Return Values (Tuple):")
name, age, student_status = get_user_info()
print(f"Name: {name}, Age: {age}, Student: {student_status}")
print()

print("2. Mathematical Calculations:")
area, circumference, diameter = calculate_circle_properties(5)
print(f"Circle with radius 5:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print(f"Diameter: {diameter}")
print()

print("3. Boolean Returns:")
numbers_to_test = [4, 7, 10, 15, 20]
for num in numbers_to_test:
    result = is_even(num)
    print(f"{num} is even: {result}")
print()

print("4. String Returns (Grades):")
scores = [95, 87, 73, 68, 45]
for score in scores:
    grade = get_grade(score)
    print(f"Score {score} = Grade {grade}")
print()

print("5. List Processing:")
test_numbers = [23, 45, 12, 89, 34, 67]
max_number = find_max_in_list(test_numbers)
print(f"Numbers: {test_numbers}")
print(f"Maximum: {max_number}")
print()

print("6. Dictionary Returns:")
pattern_info = create_pattern_info(5)
print("Pattern Information:")
for key, value in pattern_info.items():
    print(f"  {key}: {value}")
print()

print("7. Conditional Returns:")
test_nums = [-5, 0, 10]
for num in test_nums:
    num_type = check_number_type(num)
    print(f"{num} is: {num_type}")
print()

print("8. Validation with Multiple Returns:")
ages_to_validate = [-1, 15, 25, 70]
for age in ages_to_validate:
    is_valid, category = validate_age(age)
    print(f"Age {age}: Valid={is_valid}, Category={category}")
print()

print("9. Pattern Functions with Returns:")
triangle_pattern = create_triangle_pattern(4)
print("Generated Triangle Pattern:")
for line in triangle_pattern:
    print(line)
print()

print("🎉 You've mastered return values!")
print("Functions can return ANY type of data - numbers, strings, lists, dictionaries!")
print("This makes them incredibly powerful for processing and transforming data! 🚀")