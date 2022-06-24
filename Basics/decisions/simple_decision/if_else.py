# Ask the user to type which activity is performed
print("Please enter the activity to be performed.")
activity = str(input())

# Check which the activity performed and
if activity == 'calculate':
    print("Performing calculations...")
else:
    print("Performing activity...")

# Skip a line
print("")

# Show to the user that the activity is complete
print("Activity completed!")
