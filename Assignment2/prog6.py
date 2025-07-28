def print_inverted_pyramid(rows):
    """
    Prints an inverted full pyramid of asterisks.

    Args:
        rows (int): The number of rows for the pyramid (must be a positive integer).
    """
    if rows <= 0:
        print("Please enter a positive integer for the number of rows.")
        return

    # Loop from the top row (widest) down to the bottom row (single asterisk)
    # 'i' represents the current number of asterisks in the widest part of this conceptual sub-pyramid
    for i in range(rows, 0, -1):
        # Calculate the number of leading spaces needed for centering
        # As 'i' decreases, the number of stars decreases, so leading spaces increase.
        # For 'rows' = 5, 'i' goes from 5 to 1.
        # When i=5 (first row), spaces = 5 - 5 = 0
        # When i=1 (last row), spaces = 5 - 1 = 4
        spaces = rows - i

        # Calculate the number of asterisks for the current row
        # For 'rows' = 5:
        # i=5: stars = 2*5 - 1 = 9
        # i=4: stars = 2*4 - 1 = 7
        # i=3: stars = 2*3 - 1 = 5
        # i=2: stars = 2*2 - 1 = 3
        # i=1: stars = 2*1 - 1 = 1
        stars = 2 * i - 1

        # Print the spaces, then the asterisks, followed by a newline
        print(" " * spaces + "*" * stars)

def run_pyramid_program():
    """
    Prompts the user for the number of rows and prints the inverted pyramid.
    Includes input validation.
    """
    print("This program will print an inverted full pyramid of asterisks.")
    while True:
        try:
            num_rows_str = input("Enter the number of rows for the pyramid (e.g., 5): ").strip()
            if num_rows_str.lower() == 'q':
                print("Exiting program. Goodbye!")
                break

            num_rows = int(num_rows_str)
            print_inverted_pyramid(num_rows)
            break # Exit loop if input is valid and pyramid is printed
        except ValueError:
            print("Invalid input. Please enter a positive integer or 'q' to quit.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the program to get user input and print the pyramid
run_pyramid_program()
