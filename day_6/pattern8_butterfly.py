# 🎨 Pattern 8: Butterfly Pattern
# Logic: Split into two halves - top expanding, bottom contracting

rows = 5

print("🎨 Butterfly Pattern:")
print()

# Top half (including middle)
for i in range(1, rows + 1):
    # Left wing - stars
    for j in range(i):
        print("*", end=" ")
    
    # Middle spaces
    for k in range(2 * (rows - i)):
        print(" ", end=" ")
    
    # Right wing - stars
    for l in range(i):
        print("*", end=" ")
    
    print()  # New line after each row

# Bottom half (excluding middle)
for i in range(rows - 1, 0, -1):
    # Left wing - stars
    for j in range(i):
        print("*", end=" ")
    
    # Middle spaces
    for k in range(2 * (rows - i)):
        print(" ", end=" ")
    
    # Right wing - stars
    for l in range(i):
        print("*", end=" ")
    
    print()  # New line after each row 