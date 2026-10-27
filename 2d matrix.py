# 2D Matrix in Python

rows = 3
columns = 3

matrix = []

print("Enter elements for 3x3 matrix:")

# Input matrix
for i in range(rows):
    row = []

    for j in range(columns):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)

    matrix.append(row)

# Display matrix
print("\nYour 3x3 Matrix is:")

for row in matrix:
    for element in row:
        print(element, end="\t")
    print()
