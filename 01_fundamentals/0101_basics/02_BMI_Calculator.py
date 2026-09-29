# ============================================
# File : 02_BMI_Calculator.py
# Purpose:  Practice using `input()` , casting , show display for readable,
#           naming variable meaningfully
# Author: Watacharapon
# ============================================

# declaring variable 
titel = "BMI CALCULATOR RESULT"     # for use not " " overlap " " becuase use Python 3.12 up

# input
weight = float(input("Please enter your weight (kg): "))    # use flast(input) for change value is decimal
height = float(input("Please enter your height (m): "))

# process
BMI = weight / (height * height)            

# output
print(" ")
print("="*50)
print(f"{titel:^50}")                       # use for format display readable
print("="*50)
print(" ")
print(f"Weight\t\t:\t{weight} kg.")         # use `\t` format tab
print(f"Height\t\t:\t{height} m.")
print(f"Your BMI\t:\t{BMI:.2f}")            # use `.2f` format for display 2 decimal
print("="*50)