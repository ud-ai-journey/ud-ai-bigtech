# 🎨 Pattern 7: Right-Aligned Triangle with Numbers
# Logic: Print spaces first, then numbers from 1 to row number

rows = 4

print("🎨 Right-Aligned Triangle with Numbers:")
print()

for i in range(1, rows + 1):
    # Print spaces for right alignment
    for j in range(rows - i):
        print(" ", end=" ")
    
    # Print numbers from 1 to current row number
    for k in range(1, i + 1):
        print(k, end=" ")
    
    print()  # New line after each row 