# Ask the user to enter a whole number
print("Please enter a whole number.")
number = int(input())

# Check if the number the user entered is either an even or odd number and prompt the appropriate output.
if number % 2 == 0:
    print(f"The number {number} is an even number.")
elif number % 2 != 0:
    print(f"The number {number} is an odd number.")
