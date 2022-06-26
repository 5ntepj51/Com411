print("How many live cable should I avoid")
live_cables_number = int(input())

live_cables = 0

while live_cables < live_cables_number:
    print("Avoiding...", end="")
    live_cables = live_cables + 1
    print(f"Done! {live_cables} live cable avoided!")

print("")

print("All live cables have been avoided")
