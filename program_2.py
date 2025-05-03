# sum of the digits

number = int(input("Enter the numbers to do sum = "))
sum_digit = 0

while number > 0:
    digit = number % 10
    sum_digit += digit
    number = number // 10

print("sum of the digits are = ",sum_digit)