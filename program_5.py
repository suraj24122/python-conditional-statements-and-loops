# Fibonacci Series:

n = int(input("Enter the number of terms = "))

a,b = 0,1
count = 0

print("fibonacci series ")

while count < n:
    print(a, end="")
    a,b = b, a+b 
    count+=1