# ============================================
# File : 03_shopping_receipt.py
# Purpose:  Practice using `input()` , casting , show display for readable,
#           variable
# Author: Watacharapon
# ============================================

# Declaring variable
VAT = 0.07                          # VAT value constants 7% in Thailand
title = "SHOPPING RECEIPT"          # text to show as the result header escape using Nested f-strings
text_report_line1 = "Subtotal"
text_report_line2 = "Tax (7%)"
text_report_line3 = "Total"

# Input
print("Welcome to Shopping")
print(f"{"-"*5}Item 1{"-"*5}")
item_name1 = input("Enter item name : ")            # do not casting because do not calculate
price_per_unit1 = float(input("Enter price per unit (THB) : "))         # input() always returns string, so cast to float for math
quantity1 = int(input("Enter quantity (Unit) : "))                      # input() always returns string, so cast to int for math
print("")
print(f"{"-"*5}Item 2{"-"*5}")
item_name2 = input("Enter item name : ")            
price_per_unit2 = float(input("Enter price per unit (THB) : "))      
quantity2 = int(input("Enter quantity (Unit) : "))
print("")
print(f"{"-"*5}Item 3{"-"*5}")
item_name3 = input("Enter item name : ")            
price_per_unit3 = float(input("Enter price per unit (THB) : "))      
quantity3 = int(input("Enter quantity (Unit) : "))            

# Process
amount1 = price_per_unit1*quantity1
amount2 = price_per_unit2*quantity2
amount3 = price_per_unit3*quantity3

subtotal = amount1+amount2+amount3
tax_vat = subtotal*VAT
total_amount = subtotal+tax_vat

# Output
print(" ")
print("="*50)
print(f"{title:^50}")
print("="*50)
print(f"{item_name1:<25}x {price_per_unit1:<5} @ {quantity1:<7.2f}= {amount1:.2f}")
print(f"{item_name2:<25}x {price_per_unit2:<5} @ {quantity2:<7.2f}= {amount2:.2f}")
print(f"{item_name3:<25}x {price_per_unit3:<5} @ {quantity3:<7.2f}= {amount3:.2f}")
print("-"*50)
print(f"{text_report_line1:<40}:\t{subtotal:.2f}")
print(f"{text_report_line2:<40}:\t{tax_vat:.2f}")
print(f"{text_report_line3:<40}:\t{total_amount:.2f}")
print("="*50)