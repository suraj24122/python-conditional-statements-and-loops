# Find Maximum of Three Numbers:

# This program finds the maximum of three numbers using if-else statements.
# It prompts the user to enter three numbers and then compares them to determine the maximum.
# Finally, it prints the maximum number.

# Get user input for three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Determine the maximum number
if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3

# Print the maximum number
print(f"The maximum number is: {max_num}")
