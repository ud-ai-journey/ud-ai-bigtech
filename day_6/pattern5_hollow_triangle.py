# 🎨 Pattern 5: Hollow Right Triangle
# Logic: Print * only if it's first column, last column, or last row

rows = 5

print("🎨 Hollow Right Triangle Pattern:")
print()

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # Print * if: first column OR last column OR last row
        if j == 1 or j == i or i == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space for hollow area
    print()  # New line after each row 