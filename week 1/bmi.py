weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in feet: "))
height = height * 0.3048

bmi = weight / (height ** 2)

print("Your BMI is:",bmi)

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 24.9:
    print("Category: Normal weight")
elif bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")