rows=int(input("Enter number of rows to print: "))

for i in range(rows, 0, -1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
