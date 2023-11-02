marks = int(input("Enter marks(0-100): "))

if marks>90:
   grade = 'S'
elif marks>70:
   grade = 'A'
elif marks>50:
    grade = 'B'
elif marks>30:
    grade = 'C'
else:
   grade = 'F'

print("Your grade is:", grade)
