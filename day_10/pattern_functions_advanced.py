# 🎨 Day 10: Pattern Functions Advanced - From Artist to Architect
# Learning: Converting pattern expertise into reusable, powerful functions

print("🎨 Pattern Functions Advanced - Code Architecture for Artists")
print("=" * 65)

# BASIC PATTERN BUILDING BLOCKS - The Foundation Functions
def print_spaces(count):
    """Print specified number of spaces - the invisible foundation"""
    for i in range(count):
        print(" ", end="")

def print_characters(char, count):
    """Print any character multiple times - the flexible painter"""
    for i in range(count):
        print(char, end=" ")

def print_line_break():
    """Start a new line - the row separator"""
    print()

# ADVANCED PATTERN FUNCTIONS - The Master Collection
def draw_right_triangle(rows, char="*"):
    """Enhanced right triangle with customizable character"""
    print(f"🔺 Right Triangle ({rows} rows, using '{char}'):")
    for i in range(1, rows + 1):
        print_characters(char, i)
        print_line_break()
    print_line_break()

def draw_inverted_triangle(rows, char="*"):
    """Inverted triangle - the upside-down pyramid"""
    print(f"🔻 Inverted Triangle ({rows} rows, using '{char}'):")
    for i in range(rows, 0, -1):
        print_characters(char, i)
        print_line_break()
    print_line_break()

def draw_centered_triangle(rows, char="*"):
    """Centered triangle with automatic spacing calculation"""
    print(f"🔺 Centered Triangle ({rows} rows, using '{char}'):")
    for i in range(1, rows + 1):
        spaces_needed = rows - i
        print_spaces(spaces_needed)
        print_characters(char, i)
        print_line_break()
    print_line_break()

def draw_hollow_triangle(rows, char="*"):
    """Hollow triangle - only the border"""
    print(f"⭕ Hollow Triangle ({rows} rows, using '{char}'):")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            if j == 1 or j == i or i == rows:
                print(char, end=" ")
            else:
                print(" ", end=" ")
        print_line_break()
    print_line_break()

def draw_diamond(rows, char="*"):
    """Complete diamond - expansion + contraction"""
    print(f"💎 Diamond Pattern ({rows} rows, using '{char}'):")
    
    # Upper half (including middle)
    for i in range(1, rows + 1):
        spaces = rows - i
        print_spaces(spaces)
        print_characters(char, i)
        print_line_break()
    
    # Lower half
    for i in range(rows - 1, 0, -1):
        spaces = rows - i
        print_spaces(spaces)
        print_characters(char, i)
        print_line_break()
    print_line_break()

def draw_butterfly(rows, char="*"):
    """Butterfly pattern with wing logic"""
    print(f"🦋 Butterfly Pattern ({rows} rows, using '{char}'):")
    
    # Top half
    for i in range(1, rows + 1):
        # Left wing
        print_characters(char, i)
        # Middle spaces
        middle_spaces = 2 * (rows - i)
        print_spaces(middle_spaces)
        # Right wing
        print_characters(char, i)
        print_line_break()
    
    # Bottom half
    for i in range(rows - 1, 0, -1):
        # Left wing
        print_characters(char, i)
        # Middle spaces
        middle_spaces = 2 * (rows - i)
        print_spaces(middle_spaces)
        # Right wing
        print_characters(char, i)
        print_line_break()
    print_line_break()

# PATTERN ANALYSIS FUNCTIONS - The Data Scientists
def calculate_pattern_stats(rows, pattern_type="right_triangle"):
    """Calculate statistics about different patterns"""
    if pattern_type == "right_triangle":
        total_chars = sum(range(1, rows + 1))  # 1+2+3+...+n
        pattern_name = "Right Triangle"
    elif pattern_type == "inverted_triangle":
        total_chars = sum(range(1, rows + 1))
        pattern_name = "Inverted Triangle"
    elif pattern_type == "diamond":
        total_chars = sum(range(1, rows + 1)) + sum(range(1, rows))
        pattern_name = "Diamond"
    else:
        total_chars = 0
        pattern_name = "Unknown"
    
    return {
        "pattern": pattern_name,
        "rows": rows,
        "total_characters": total_chars,
        "average_per_row": total_chars / rows if rows > 0 else 0
    }

def generate_pattern_as_string(rows, pattern_type="right_triangle", char="*"):
    """Generate pattern as string instead of printing directly"""
    lines = []
    
    if pattern_type == "right_triangle":
        for i in range(1, rows + 1):
            line = (char + " ") * i
            lines.append(line.strip())
    elif pattern_type == "centered_triangle":
        for i in range(1, rows + 1):
            spaces = " " * (rows - i)
            chars = (char + " ") * i
            line = spaces + chars.strip()
            lines.append(line)
    
    return lines

# PATTERN COMBINATION FUNCTIONS - The Creative Director
def draw_multiple_patterns(rows, patterns_list, char="*"):
    """Draw multiple patterns in sequence"""
    print(f"🎨 Pattern Gallery ({rows} rows each, using '{char}'):")
    print("=" * 60)
    
    pattern_functions = {
        "right": draw_right_triangle,
        "inverted": draw_inverted_triangle,
        "centered": draw_centered_triangle,
        "hollow": draw_hollow_triangle,
        "diamond": draw_diamond,
        "butterfly": draw_butterfly
    }
    
    for pattern in patterns_list:
        if pattern in pattern_functions:
            pattern_functions[pattern](rows, char)
        else:
            print(f"❓ Unknown pattern: {pattern}")

def create_custom_pattern(rows, instructions):
    """Create pattern based on custom instructions"""
    print(f"🎯 Custom Pattern ({rows} rows):")
    
    for row in range(1, rows + 1):
        line = ""
        for instruction in instructions:
            if instruction == "spaces":
                line += " " * (rows - row)
            elif instruction == "stars":
                line += "* " * row
            elif instruction == "numbers":
                line += " ".join(str(i) for i in range(1, row + 1))
            elif instruction == "reverse_numbers":
                line += " ".join(str(i) for i in range(row, 0, -1))
        
        print(line)
    print()

# TESTING THE PATTERN FUNCTION LIBRARY - The Art Gallery!
print("\n🖼️ PATTERN FUNCTION GALLERY:")
print("-" * 50)

print("1. Basic Patterns with Different Characters:")
draw_right_triangle(4, "⭐")
draw_inverted_triangle(4, "🔥")
draw_centered_triangle(4, "💎")

print("2. Advanced Patterns:")
draw_hollow_triangle(5)
draw_diamond(4, "❤️")

print("3. Complex Patterns:")
draw_butterfly(4, "🦋")

print("4. Pattern Statistics:")
stats = calculate_pattern_stats(5, "right_triangle")
print("Right Triangle Stats:")
for key, value in stats.items():
    print(f"  {key}: {value}")

diamond_stats = calculate_pattern_stats(4, "diamond")
print("\nDiamond Stats:")
for key, value in diamond_stats.items():
    print(f"  {key}: {value}")
print()

print("5. Pattern as String Data:")
triangle_strings = generate_pattern_as_string(3, "right_triangle", "#")
print("Generated Triangle as List:")
for i, line in enumerate(triangle_strings, 1):
    print(f"Row {i}: '{line}'")
print()

print("6. Multiple Pattern Gallery:")
pattern_showcase = ["right", "centered", "hollow"]
draw_multiple_patterns(3, pattern_showcase, "🌟")

print("7. Custom Pattern Creation:")
create_custom_pattern(4, ["spaces", "numbers"])
create_custom_pattern(3, ["stars"])

# FUNCTION BENEFITS DEMONSTRATION
print("🎯 BENEFITS OF PATTERN FUNCTIONS:")
print("-" * 40)
print("✅ Reusability: Write once, use anywhere")
print("✅ Customization: Different sizes, characters, styles")
print("✅ Modularity: Mix and match functions")
print("✅ Maintainability: Fix bugs in one place")
print("✅ Scalability: Easy to add new patterns")
print("✅ Data Processing: Generate patterns as data, not just output")
print()

print("🎉 You've transformed from Pattern Artist to Code Architect!")
print("Your functions are now reusable, flexible, and powerful! 🏗️✨")