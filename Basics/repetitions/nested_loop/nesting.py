print("Please enter a sequence")
sequences = str(input())

print("Please enter the character for the marker")
characters = str(input())

for sequence in range(0, len(sequences), 1):
    for character in range(0, len(characters), 1):
        print(f"The distance between the markers is {len(sequences) - 2}")
