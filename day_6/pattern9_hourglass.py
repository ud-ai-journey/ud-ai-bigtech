# 🎨 Pattern 9: Hourglass Pattern (Diamond Inverted)
# Logic: Top half decreasing, bottom half increasing

rows = 5

print("🎨 Hourglass Pattern:")
print()

# Top half (including middle)
for i in range(rows, 0, -1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end=" ")
    
    # Print stars
    for k in range(i):
        print("*", end=" ")
    
    print()  # New line after each row

# Bottom half (excluding middle)
for i in range(2, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end=" ")
    
    # Print stars
    for k in range(i):
        print("*", end=" ")
    
    print()  # New line after each row 