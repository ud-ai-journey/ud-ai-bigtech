# Inverted Triangle Pattern
# Prints an inverted triangle using stars

rows = int(input("Enter the number of rows: "))

print("\nInverted Triangle Pattern:")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nExample with 5 rows:")
print("* * * * * ")
print("* * * * ")
print("* * * ")
print("* * ")
print("* ") 