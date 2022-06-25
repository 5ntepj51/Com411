# Ask the user to enter the first whole number
print("Please enter the first whole number")
first_number = int(input())

# Ask the user to enter the second whole number
print("Please enter the second whole number")
second_number = int(input())

# Ask the user to enter a third whole number
print("please enter the third whole number")
third_number = int(input())

odd_number = 0
even_number = 0

if first_number % 2 == 0:
    even_number = even_number + 1

elif first_number % 2 == 1:
    odd_number = odd_number + 1

if second_number % 2 == 0:
    even_number = even_number + 1

elif second_number % 2 == 1:
    odd_number = odd_number + 1

if third_number % 2 == 0:
    even_number = even_number + 1

elif third_number % 2 == 1:
    odd_number = odd_number + 1


print(f"There were {even_number} even and {odd_number} odd numbers.")
