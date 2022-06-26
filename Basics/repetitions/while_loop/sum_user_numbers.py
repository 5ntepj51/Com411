print("How many numbers should I sum up?")
user_number = int(input())

number = 0
total = 0

while number < user_number:
    print(f"Please enter number {number} of {user_number}")
    next_number = int(input())
    total = total + next_number
    number = number + 1

print(f"The answer is {total}")
