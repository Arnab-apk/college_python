def is_palindrome_number(num_str):
    """
    Checks if a given string representation of a number is a palindrome.

    Args:
        num_str (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return num_str == num_str[::-1]

def run_palindrome_checker():
    """
    Continuously takes input from the user until 'q' or 'Q' is entered.
    Checks if the input is a number and if it's a palindrome, then prints it.
    """
    print("Enter numbers to check if they are palindromes.")
    print("Type 'q' (or 'Q') and press Enter to quit.")

    while True:
        user_input = input("Enter a number (or 'q' to quit): ").strip()

        # Check for quit condition (case-insensitive)
        if user_input.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break

        # Check if the input is a valid integer
        if user_input.isdigit():
            # If it's a positive integer, check if it's a palindrome
            if is_palindrome_number(user_input):
                print(f"'{user_input}' is a palindrome number!")
            else:
                print(f"'{user_input}' is not a palindrome number.")
        elif user_input.startswith('-') and user_input[1:].isdigit():
            # Handle negative numbers (e.g., "-121" is considered a palindrome if "121" is)
            # For strict numerical palindrome, negative numbers are usually not considered.
            # Here, we check the absolute value's string representation.
            absolute_value_str = user_input[1:]
            if is_palindrome_number(absolute_value_str):
                print(f"'{user_input}' (absolute value '{absolute_value_str}') is a palindrome number!")
            else:
                print(f"'{user_input}' is not a palindrome number.")
        else:
            print(f"'{user_input}' is not a valid number. Please enter an integer or 'q'.")

# Run the palindrome checker
run_palindrome_checker()
