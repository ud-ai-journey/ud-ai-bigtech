# Right-Angled Triangle Pattern
# Prints a right-angled triangle using stars

rows = int(input("Enter the number of rows: "))

print("\nRight-Angled Triangle Pattern:")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nExample with 5 rows:")
print("* ")
print("* * ")
print("* * * ")
print("* * * * ")
print("* * * * * ") 