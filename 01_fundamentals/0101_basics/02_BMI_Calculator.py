# ============================================
# File : 02_BMI_Calculator.py
# Purpose:  Practice using `input()` , casting , show display for readable,
#           naming variable meaningfully
# Author: Watacharapon
# ============================================

# declaring variable 
title = "BMI CALCULATOR RESULT"             # text to show as the result header

# input
weight = float(input("Please enter your weight (kg): "))    # input() always returns string, so cast to float for math
height = float(input("Please enter your height (m): "))     # same reason as above

# process
bmi = weight / (height * height)            # BMI formula: weight divided by height squared

# output
print(" ")
print("="*50)
print(f"{title:^50}")                       # :^50 centers the text in a 50-character width
print("="*50)
print(" ")
print(f"Weight\t\t:\t{weight} kg.")         # \t adds a tab space for alignment
print(f"Height\t\t:\t{height} m.")
print(f"Your BMI\t:\t{bmi:.2f}")            # :.2f rounds the number to 2 decimal places
print("="*50)