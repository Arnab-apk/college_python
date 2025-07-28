def factorial_recursive(n):
    """
    Calculates the factorial of a number using recursion.

    Args:
        n (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of n.
        str: An error message if n is negative.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        # Recursive step: n! = n * (n-1)!
        return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """
    Calculates the factorial of a number using an iterative (non-recursive) method.

    Args:
        n (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of n.
        str: An error message if n is negative.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        result = 1
        # Multiply result by each integer from 1 to n
        for i in range(1, n + 1):
            result *= i
        return result

def run_factorial_program():
    """
    Prompts the user for a number and calculates its factorial
    using both recursive and iterative methods.
    """
    while True:
        try:
            num_str = input("Enter a non-negative integer to find its factorial (or 'q' to quit): ").strip()
            if num_str.lower() == 'q':
                print("Exiting program. Goodbye!")
                break

            num = int(num_str)

            print(f"\nCalculating factorial for {num}:")

            # Calculate using recursive method
            recursive_result = factorial_recursive(num)
            print(f"  Recursive Method: {recursive_result}")

            # Calculate using iterative method
            iterative_result = factorial_iterative(num)
            print(f"  Iterative Method: {iterative_result}")

        except ValueError:
            print("Invalid input. Please enter a non-negative integer or 'q'.")
        except RecursionError:
            # This can happen for very large numbers with recursion due to Python's recursion limit
            print("Recursion depth limit exceeded. Try a smaller number for the recursive method.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the program
run_factorial_program()
