# Grade System

# Input: Marks from the user
marks = int(input("Enter your marks: "))

# Determine the grade based on marks
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

# Output: Display the grade
print(f"Your grade is: {grade}")