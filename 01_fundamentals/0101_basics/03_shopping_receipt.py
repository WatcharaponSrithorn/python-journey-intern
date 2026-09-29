# ============================================
# File : 03_shopping_receipt.py
# Purpose:  Practice using `input()` , casting , show display for readable,
#           variable
# Author: Watacharapon
# ============================================

# Declaring variable
VAT = 7                         # VAT value constants 7% in Thailand
title = "SHOPPING RECEIPT"      # text to show as the result header escape using Nested f-strings

# Input
print("Wellcome to Shopping")
print(f"{"-"*5}Item 1{"-"*5}")
item_name1 = input("Enter item name : ")            # do not casting because do not calculate
price_per_unit1 = float(input("Enter price per unit (THB) : "))      # input() always returns string, so cast to float for math
quantity1 = float(input("Enter quantity (Unit) : "))                 # same above
print("")
print(f"{"-"*5}Item 2{"-"*5}")
item_name2 = input("Enter item name : ")            
price_per_unit2 = float(input("Enter price per unit (THB) : "))      
quantity2 = float(input("Enter quantity (Unit) : "))
print("")
print(f"{"-"*5}Item 3{"-"*5}")
item_name3 = input("Enter item name : ")            
price_per_unit3 = float(input("Enter price per unit (THB) : "))      
quantity3 = float(input("Enter quantity (Unit) : "))            

# Process
amount1 = price_per_unit1*quantity1
amount2 = price_per_unit2*quantity2
amount3 = price_per_unit3*quantity3

subtotal = amount1+amount2+amount3
tax_vat = (subtotal*VAT)/100
total_amount = subtotal+tax_vat

# Output
print(" ")
print("="*50)
print(f"{title:^50}")
print("="*50)
print(f"{item_name1:<20}\tx{price_per_unit1}\t@{quantity1}\t= {amount1}")
print(f"{item_name2:<20}\tx{price_per_unit2}\t@{quantity2}\t= {amount2}")
print(f"{item_name3:<20}\tx{price_per_unit3}\t@{quantity3}\t= {amount3}")
print("-"*50)
print(f"Subtotal\t\t\t:{subtotal}")
print(f"Tax (7%)\t\t\t:{tax_vat}")
print(f"Total (7%)\t\t\t:{total_amount}")
print("="*50)