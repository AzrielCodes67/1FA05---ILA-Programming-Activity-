"""
Program: Distance Between Two Points Calculator
Author: [Your Name]
Date: [Current Date]
Description: Calculates the Euclidean distance between two points (x1, y1) and (x2, y2)
             using Python's math library functions sqrt() and pow().
"""

import math

# --- 1. USER INPUT ---
# Prompt user to enter coordinates for the two points
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# --- 2. DISTANCE CALCULATION ---
# Applying the Euclidean distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# --- 3. OUTPUT ---
# Display the computed result formatted to 2 decimal places
print()
print(f"The distance between the two points is: {distance:.2f}")

# ==============================================================================
# REFLECTION:
# Using a library is much more practical than writing calculations from scratch 
# because functions like math.sqrt() and math.pow() are already optimized and 
# ready to use. In this activity, the math library allowed us to compute complex 
# square roots and exponents in a single line of code without manually writing 
# the underlying mathematical algorithms. Without these functions, calculating a 
# square root would require writing extra complex code, making the program harder 
# to build and maintain.
# ==============================================================================