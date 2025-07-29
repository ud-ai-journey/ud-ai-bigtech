# Diamond Pattern
# Prints a diamond shape using stars

rows = int(input("Enter the number of rows (use odd number for perfect diamond): "))

print("\nDiamond Pattern:")

# Upper half of diamond
for i in range(1, rows//2 + 2):
    # Print spaces
    for j in range(rows//2 + 1 - i):
        print(" ", end="")
    # Print stars
    for k in range(2*i - 1):
        print("*", end="")
    print()

# Lower half of diamond
for i in range(rows//2, 0, -1):
    # Print spaces
    for j in range(rows//2 + 1 - i):
        print(" ", end="")
    # Print stars
    for k in range(2*i - 1):
        print("*", end="")
    print()

print("\nExample with 7 rows:")
print("   *")
print("  ***")
print(" *****")
print("*******")
print(" *****")
print("  ***")
print("   *") 