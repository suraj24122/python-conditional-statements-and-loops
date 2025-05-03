# Print Multiplication Table

number = int(input("Enter the number to print multiplication table = "))

for i in range(1, 11):
    print(f"{number} X {i} = {number * i}")