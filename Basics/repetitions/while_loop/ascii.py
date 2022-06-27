print("How many bars should be charged?")
battery_level = int(input())

charged = 0

while charged < battery_level:
      charged = charged + 1
      print(f"Charging:{' █' * charged}")

print("")

print("The battery is fully charged.")