# ============================================
# File : 09_Sales_Row_Checker.py
# Purpose:  Practice using For Loop basic if input 
#           check data quality many rows before saving data
#           summarize how many rows passed and failed.
#           pass add sum Total sales  
# Author: Watacharapon
# ============================================

# Declare varible
# variable for display
title_program = "Sales Row Quality Checker"
separator = "="
hyphen = "-"
result_row = ""
title_summary = "SUMMARY"
display_summary_1 = "Rows passed"
display_summary_2 = "Rows failed"
display_summary_3 = "Total sales (passed):"
# variable for calculate
total = 0
row_pass = 0
row_fail = 0

# Section input ask number of rows
print(f"{separator*5} {title_program} {separator*5}")
number_row = int(input("How many rows to check (1-10) : "))
# Section check number row if is in range will receive for verify pass or faile.
if 1 <= number_row <= 10:
    for i in range(1,number_row+1):     # need start 1
        print(f"{hyphen*5} Row {i} {hyphen*5}")
        product_name = input("Enter product name : ")
        unit_price = float(input("Enter unit price (THB) : "))
        quantity = int(input("Enter quantity : "))
        # # Section check dat quality and if pass will calculate next then
        if product_name == "":
            row_fail += 1
            result_row = "FAIL: product name is empty"
        elif unit_price <= 0:
            row_fail += 1
            result_row = "FAIL: price must be more than 0"
        elif quantity <= 0:
            row_fail += 1
            result_row = "FAIL: quantity must be more than 0"
        else:
            row_pass += 1
            total += unit_price*quantity
            result_row = "PASS"
        print(f"{hyphen*17}")
        print(f"Row {i} : {result_row}")
    # Section display summary
    print(f"{separator*50}")
    print(f"{separator*5} {title_summary} {separator*5} ")
    print(f"{display_summary_1:<25} : {row_pass}")
    print(f"{display_summary_2:<25} : {row_fail}")
    print(f"{display_summary_3:<25} : {total:.2f}")
    print(f"{separator*50}")
else:
    print("Invalid")

