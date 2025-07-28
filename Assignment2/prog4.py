def is_palindrome(num):
    return str(num) == str(num)[::-1]

while True:
    inp = input("Enter a number (or 'q' to quit): ")
    if inp.lower() == 'q':
        break
    if inp.isdigit() and is_palindrome(inp):
        print(inp, "is a palindrome.")
    else:
        print(inp, "is not a plaindrome number")
