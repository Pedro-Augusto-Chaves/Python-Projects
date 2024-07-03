height = float(input("Digit your height: "))
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input("Digit your weight: "))

bmi = int(weight / height**2)
print(bmi)

if bmi >= 35:
    print("You are clinically obese")
elif bmi >= 30:
    print("You are obese")
elif bmi >= 25:
    print("You are slightly overweight")
elif bmi >= 18.5:
    print("You have a normal weight")
else:
    print("You are underweight")