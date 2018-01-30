# Function that takes the height and weight as arguments and returns the BMI, all as floats

import math

def BMI (gender = "female", weight_lbs="168.5", height_inches=63.7):
	"""
	Calculate the BMI using as input height (inches) and weight (pounds). 
	Default arguments are based on average female in the United States, as reported by the CDC.
	https://www.cdc.gov/nchs/fastats/body-measurements.htm
	"""

	BMI = (float(weight_lbs) * 0.453592)  / math.pow((float(height_inches) * 0.0254), 2)
	return BMI

# height_inches = int(input("What is your height in inches: "))
# weight_lbs = int(input("What is your weight in pounds: "))
# print(BMI(height_inches, weight_lbs))

import sys

height_inches=float(sys.argv[1])
weight_lbs=float(sys.argv[2])

print(BMI(height_inches, weight_lbs))