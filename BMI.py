# BMI CALCULATOR

height = float(input("enter height :\n"))

weight = float(input("enter weight:\n"))

BMI = weight / height**2


if BMI >= 35:
    print("Clinically Obese")
elif BMI >= 30:
    print("Obese")
elif BMI >= 25:
    print("Slightly over weight")
elif BMI >= 18.5:
    print("Normal Weight")
else:
    print("Under Weight")


