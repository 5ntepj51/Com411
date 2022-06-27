
print("What level of brightness is required?")
level = int(input())

print("\nAdjusting brightness...\n")
print()


for level in range(2, level + 1, 2):
    print(f"Beep's brightness level: {'*' * level} ")

    print(f"Bop's brightness level {'*' * level}")

print()

print("Adjustments complete!")
