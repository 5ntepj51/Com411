print("Program Started!")

print("")

print("Please enter a ASCII code")
ascii_code = int(input())

if ascii_code in range(32, 127):
    print(f"The characters represented by the ASCII code {ascii_code} is: {chr(ascii_code)}")

else:
    print("Error! Please enter another ASCII code")

print("")

print("Program Ended!")
