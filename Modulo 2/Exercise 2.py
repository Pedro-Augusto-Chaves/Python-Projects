#Write a program that calculates the Body Mass Index (BMI) from a user's weight and heigh
# 1st input: enter height in meters e.g: 1.65
height = float(input("Digit your height: "))
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input("Digit your weight: "))

bmi = int(weight / height**2)
print(bmi)