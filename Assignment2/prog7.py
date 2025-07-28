def get_upright_number_pyramid_string(rows):
    """
    Generates the string representation of an upright full pyramid of numbers.

    Args:
        rows (int): The number of rows for the pyramid.

    Returns:
        str: The string containing the upright pyramid.
    """
    if rows <= 0:
        return "Please enter a positive integer for the number of rows for the upright pyramid."

    pyramid_output = "\n--- Upright Number Pyramid ---\n"
    for i in range(1, rows + 1):
        # Add leading spaces for centering
        pyramid_output += "  " * (rows - i) # Two spaces for better alignment

        # Add numbers in ascending order
        for j in range(1, i + 1):
            pyramid_output += f"{j} "

        # Add numbers in descending order (excluding the peak number)
        for j in range(i - 1, 0, -1):
            pyramid_output += f"{j} "

        pyramid_output += "\n" # Move to the next line

    return pyramid_output

def get_inverted_number_pyramid_string(rows):
    """
    Generates the string representation of an inverted full pyramid of numbers.

    Args:
        rows (int): The number of rows for the pyramid.

    Returns:
        str: The string containing the inverted pyramid.
    """
    if rows <= 0:
        return "Please enter a positive integer for the number of rows for the inverted pyramid."

    pyramid_output = "\n--- Inverted Number Pyramid ---\n"
    for i in range(rows, 0, -1):
        # Add leading spaces for centering
        pyramid_output += "  " * (rows - i) # Two spaces for better alignment

        # Add numbers in ascending order
        for j in range(1, i + 1):
            pyramid_output += f"{j} "

        # Add numbers in descending order (excluding the peak number)
        for j in range(i - 1, 0, -1):
            pyramid_output += f"{j} "

        pyramid_output += "\n" # Move to the next line

    return pyramid_output

def run_pyramid_program():
    """
    Prompts the user for the number of rows, generates both
    upright and inverted number pyramid strings, and prints them.
    """
    print("This program will generate an upright and an inverted full pyramid of numbers.")
    while True:
        try:
            num_rows_str = input("Enter the number of rows for the pyramids (e.g., 5, or 'q' to quit): ").strip()
            if num_rows_str.lower() == 'q':
                print("Exiting program. Goodbye!")
                break

            num_rows = int(num_rows_str)

            if num_rows <= 0:
                print("Please enter a positive integer for the number of rows.")
                continue

            # Get the string representation of the upright pyramid
            upright_pyramid_str = get_upright_number_pyramid_string(num_rows)

            # Get the string representation of the inverted pyramid
            inverted_pyramid_str = get_inverted_number_pyramid_string(num_rows)

            # Print both pyramids together with a single print statement
            print(upright_pyramid_str + inverted_pyramid_str)

            print("\nPyramids generated and printed successfully!")
            break # Exit loop after successful execution
        except ValueError:
            print("Invalid input. Please enter a positive integer or 'q'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the main program
run_pyramid_program()
