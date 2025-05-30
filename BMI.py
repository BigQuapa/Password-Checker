Weight = int(input("Please enter your weight in lbs: "))
Height = int(input("Now please enter your height in inches: "))
weight_kg = Weight * 0.453592
Height_meters = Height * 0.0254
BMI = float(weight_kg/Height_meters**2)
print("Your current BMI is: ", BMI)