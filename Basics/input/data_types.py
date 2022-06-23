# Ask the user to enter his name
print("What is your name human?")
name = str(input())

# Ask the user to type in his age
print("How old are you (in years)?")
age = int(input())

# Ask the user to enter his height in meters
print("How tall are you(in meters)?")
height = float(input())

# Ask the user to enter his weight in Kilograms
print("How much do you weigh(in Kilograms)?")
weigh = float(input())

# Make a calculation of the user Bmi with the information he provided
bmi = "{:.2f}".format(float(weigh / (height ** 2)))

# Output the name of the user with his BMI
print(f"{name} you are {age} old and your bmi is {bmi}")
