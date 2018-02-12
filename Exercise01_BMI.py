# Write a Python program that uses input() to read weight and height values from the user and compute their BMI.

import math 

weight_kg = input("Enter weight in kilograms: ")
height_meters = input("Enter height in meters: ")

BMI = float(weight_kg) / math.pow(float(height_meters), 2)
print("The BMI of an individual who is", weight_kg, "kilograms and", height_meters, "meters is", BMI)

# Optional challenge:  read the weight and height in non-metric units.

weight_lbs = input("Enter weight in pounds: ")
height_inches = input("Enter height in inches: ")

BMI = (float(weight_lbs) * 0.453592)  / math.pow((float(height_inches) * 0.0254), 2)
print("The BMI of an individual who is", weight_lbs, "pounds and", height_inches, "inches is", BMI)
