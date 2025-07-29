# Number Pyramid Pattern
# Prints a pyramid using numbers

rows = int(input("Enter the number of rows: "))

print("\nNumber Pyramid Pattern:")
for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # Print ascending numbers
    for k in range(1, i + 1):
        print(k, end="")
    
    # Print descending numbers
    for l in range(i - 1, 0, -1):
        print(l, end="")
    
    print()

print("\nExample with 5 rows:")
print("    1")
print("   121")
print("  12321")
print(" 1234321")
print("123454321") 