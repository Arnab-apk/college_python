n = int(input("How many numbers? "))
numbers = []

for _ in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers = list(set(numbers))  # remove duplicates
numbers.sort(reverse=True)

if len(numbers) >= 2:
    print("Second largest number is:", numbers[1])
else:
    print("Not enough unique numbers.")
