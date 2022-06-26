print("Please enter a number?")
user_number = int(input())

number = 0
factorial = 1

while number < user_number:
    number = number + 1
    factorial = factorial * number

print(f"The factorial is {factorial}.")
