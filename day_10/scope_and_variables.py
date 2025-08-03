# 🌍 Day 10: Scope & Variables - The Territory Rules
# Learning: Local vs Global scope, variable accessibility, and best practices

print("🌍 Scope & Variables - Understanding Territory Rules")
print("=" * 55)

# GLOBAL VARIABLES - The Public Park
company_name = "TechCorp"  # Global - accessible everywhere
total_employees = 100      # Global - shared by all functions

def demonstrate_global_access():
    """Function accessing global variables - like reading a public billboard"""
    print(f"Company: {company_name}")
    print(f"Total Employees: {total_employees}")
    print("✅ Functions can READ global variables")

# LOCAL VARIABLES - The Private Office
def demonstrate_local_variables():
    """Function with local variables - like having a private workspace"""
    department = "Engineering"      # Local to this function
    local_employees = 25           # Local to this function
    
    print(f"Department: {department}")
    print(f"Local Team: {local_employees}")
    print("✅ Local variables exist only inside the function")
    
    # We can also access globals from here
    print(f"We're part of {company_name}")

# VARIABLE SHADOWING - The Name Collision
total_employees_global = 100  # Global version

def demonstrate_shadowing():
    """Function showing variable shadowing - local variable hides global"""
    total_employees_global = 50  # Local variable with same name!
    
    print(f"Inside function: {total_employees_global}")  # Shows local value (50)
    print("⚠️ Local variable 'shadows' (hides) the global one")

# MODIFYING GLOBAL VARIABLES - The Permission System
global_counter = 0

def increment_counter_wrong():
    """Attempting to modify global without permission - FAILS!"""
    try:
        global_counter = global_counter + 1  # This creates a LOCAL variable!
        print(f"Inside function: {global_counter}")
    except UnboundLocalError as e:
        print(f"❌ Error: {e}")
        print("Can't modify global without 'global' keyword!")

def increment_counter_correct():
    """Correctly modifying global variable - with permission"""
    global global_counter  # Getting permission to modify global
    global_counter = global_counter + 1
    print(f"✅ Global counter now: {global_counter}")

# FUNCTION PARAMETERS - The Input Gate
def process_data(input_value):
    """Parameters are local variables created automatically"""
    input_value = input_value * 2  # Modifying parameter (local copy)
    print(f"Inside function: {input_value}")
    return input_value

# PATTERN FUNCTIONS WITH SCOPE AWARENESS
pattern_symbol = "*"  # Global pattern symbol

def draw_line_with_global(length):
    """Using global variable inside function"""
    line = pattern_symbol * length
    print(line)

def draw_line_with_parameter(length, symbol):
    """Using parameter instead of global - more flexible!"""
    line = symbol * length
    print(line)

def create_pattern_data(rows):
    """Function creating local data and returning it"""
    pattern_lines = []  # Local list
    line_count = 0      # Local counter
    
    for i in range(1, rows + 1):
        line = "* " * i
        pattern_lines.append(line)
        line_count += 1
    
    # Return local data (it survives outside the function!)
    return pattern_lines, line_count

# NESTED FUNCTIONS - The Building Within Building
def outer_function():
    """Outer function with inner function - like a building with rooms"""
    outer_variable = "I'm from outer function"
    
    def inner_function():
        """Inner function can access outer function's variables"""
        inner_variable = "I'm from inner function"
        print(f"Inner sees: {outer_variable}")  # Can see outer
        print(f"Inner has: {inner_variable}")
    
    print(f"Outer has: {outer_variable}")
    inner_function()  # Call the inner function
    # print(inner_variable)  # This would cause an error!

# TESTING SCOPE CONCEPTS - The Territory Explorer!
print("\n🗺️ SCOPE EXPLORATION:")
print("-" * 40)

print("1. Global Variable Access:")
demonstrate_global_access()
print()

print("2. Local Variables in Action:")
demonstrate_local_variables()
print()

print("3. Variable Shadowing:")
print(f"Before function: {total_employees_global}")
demonstrate_shadowing()
print(f"After function: {total_employees_global}")  # Still original value!
print()

print("4. Modifying Global Variables:")
print(f"Counter before: {global_counter}")
print("Trying wrong way:")
increment_counter_wrong()
print(f"Counter still: {global_counter}")
print("Trying correct way:")
increment_counter_correct()
print()

print("5. Function Parameters and Local Copies:")
original_value = 10
print(f"Original value: {original_value}")
result = process_data(original_value)
print(f"Returned value: {result}")
print(f"Original unchanged: {original_value}")
print()

print("6. Pattern Functions with Different Scope Approaches:")
print("Using global variable:")
draw_line_with_global(5)
print("Using parameters (better approach):")
draw_line_with_parameter(5, "#")
draw_line_with_parameter(5, "❤️")
print()

print("7. Creating and Returning Local Data:")
pattern_data, count = create_pattern_data(3)
print(f"Created {count} lines:")
for line in pattern_data:
    print(line)
print()

print("8. Nested Functions:")
outer_function()
print()

# SCOPE BEST PRACTICES SUMMARY
print("🎯 SCOPE BEST PRACTICES:")
print("-" * 30)
print("✅ Use parameters instead of global variables when possible")
print("✅ Keep variables in the smallest scope needed")
print("✅ Use 'global' keyword only when necessary")
print("✅ Prefer returning values over modifying globals")
print("✅ Give variables clear, descriptive names")
print()

print("🎉 You now understand the Territory Rules of Programming!")
print("Scope is like having different access levels in a building! 🏢")