# 🎨 Pattern 6: Number Pyramid with Incrementing Digits
# Logic: Continue incrementing number across all rows

rows = 4
num = 1  # Starting number

print("🎨 Number Pyramid with Incrementing Digits:")
print()

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1  # Increment for next position
    print()  # New line after each row 