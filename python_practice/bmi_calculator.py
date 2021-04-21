height = float(input("What is your height in meters?: "))
weight = int(input("What is your weight in Kg?: "))
bmi = weight / (height * height)

if bmi < 30:
    if bmi >= 25:
        print("Overweight")
    if bmi >= 18.5:
        print("Normal")
    if bmi < 18.5:
        print("Underweight")
else:
    print("Obesity")