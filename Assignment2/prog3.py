def find_second_largest():
    """
    Prompts the user to enter N numbers, then finds and prints the second largest number.
    Handles cases with less than two unique numbers.
    """
    while True:
        try:
            n = int(input("How many numbers do you want to enter (N)? "))
            if n <= 0:
                print("Please enter a positive integer for N.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    numbers = []
    print(f"Please enter {n} numbers:")
    for i in range(n):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Convert the list to a set to get unique numbers, then convert back to a list
    unique_numbers = sorted(list(set(numbers)))

    if len(unique_numbers) < 2:
        print("There are not enough unique numbers to determine a second largest number.")
        if unique_numbers:
            print(f"The largest (and only unique) number is: {unique_numbers[0]}")
    else:
        # The second largest number will be at index -2 after sorting unique numbers in ascending order
        second_largest = unique_numbers[-2]
        print(f"The numbers entered are: {numbers}")
        print(f"The unique numbers (sorted) are: {unique_numbers}")
        print(f"The second largest number is: {second_largest}")

# Call the function to run the program
find_second_largest()
