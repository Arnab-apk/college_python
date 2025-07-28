import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
sqrt_num = math.sqrt(num)

if sqrt_num.is_integer() and is_prime(int(sqrt_num)):
    print("Square root is prime.")
else:
    print("Square root is not prime.")
