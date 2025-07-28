def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Function switch using dictionary
def calculate_factorial(method, number):
    switch = {
        '1': factorial_recursive,
        '2': factorial_iterative
    }
    if method in switch:
        return switch[method](number)
    else:
        return "Invalid result!"

# User input
n = int(input("Enter a number: "))
print("Choose method to calculate factorial:")
print("1. Recursive")
print("2. Iterative")

choice = input("Enter choice (1 or 2): ")
result = calculate_factorial(choice, n)
print("Factorial:", result)
