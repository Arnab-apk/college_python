import math

def is_prime(n):
    """
    Checks if a number is prime.
    A number is prime if it is greater than 1 and has no divisors other than 1 and itself.
    """
    # Prime numbers must be greater than 1.
    if n <= 1:
        return False
    # 2 is the only even prime number.
    if n == 2:
        return True
    # All other even numbers are not prime.
    if n % 2 == 0:
        return False
    # Check for odd divisors from 3 up to the square root of n.
    # We only need to check up to the square root because if n has a divisor larger
    # than its square root, it must also have a smaller one.
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def check_sqrt_prime():
    """
    Main function to get user input, calculate the square root,
    and check if the square root is a prime number.
    This version does not have error handling.
    """
    # Get input from the user.
    num_str = input("Enter a number: ")
    num = float(num_str)

    # Handle negative numbers, which don't have real square roots.
    if num < 0:
        print(f"Cannot calculate the real square root of a negative number ({num}).")
        return

    # Calculate the square root.
    sqrt_num = math.sqrt(num)

    # Check if the square root is a whole number (integer).
    # A prime number must be an integer.
    if sqrt_num != int(sqrt_num):
        print(f"The square root of {num} is {sqrt_num:.4f}, which is not a whole number.")
        print("Therefore, the square root of your number cannot be prime.")
    else:
        # If it's a whole number, cast it to an integer.
        int_sqrt = int(sqrt_num)
        print(f"The square root of {num} is the whole number {int_sqrt}.")
        
        # Check if this integer is a prime number.
        if is_prime(int_sqrt):
            print(f"The number {int_sqrt} is a prime number.")
        else:
            print(f"The number {int_sqrt} is NOT a prime number.")

# --- Run the program ---
check_sqrt_prime()
