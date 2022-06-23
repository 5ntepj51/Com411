# Ask the user to enter the number of lives.
print("Please enter the number of lives.")
numbers_of_lives = int(input()) * "♥"

# Ask the user to enter the energy level
print("Please enter the energy level.")
energy_level = int(input()) * "♦"

# Ask the user to type the shield level
print("Please enter the shield level.")
shield_level = int(input()) * "♦"

# Notified the user that the health is set up
print(f"Health has been set.")

# Skip a line and show a blank space
print("")

# Show the number of lives
print(f"Lives:  {numbers_of_lives}  ")

# Show the energy level
print(f"Energy: {energy_level} ")

# Show the shield level
print(f"Shield: {shield_level} ")
