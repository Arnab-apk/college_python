# Input: a specific year
year = int(input("Enter a year: "))
# Check if it is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    
    print(f"{year} is a Leap Year.")
else:
    
    print(f"{year} is not a Leap Year.")

# Correct time conversions
days=year*365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# Output
print(f"Total days in the year: {days}")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
