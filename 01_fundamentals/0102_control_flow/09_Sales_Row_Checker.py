# ============================================
# File : 09_Sales_Row_Checker.py
# Purpose:  Practice for loop with range() and if/elif/else to check sales rows
#           check data quality many rows before saving data
#           summarize how many rows passed and failed.
#           pass add sum Total sales  
# Author: Watacharapon
# ============================================

# Declare variable
# variable for display
title_program = "Sales Row Quality Checker"
separator = "="
hyphen = "-"
result_row = ""
title_summary = "SUMMARY"
display_summary_1 = "Rows passed"
display_summary_2 = "Rows fail"
display_summary_3 = "Total sales (passed)"
# variable for calculate
# Set counters BEFORE the loop. If we set them inside the loop,
# they would reset to 0 on every round and the totals would be wrong.
total = 0
row_pass = 0
row_fail = 0

# Section input ask number of rows
print(f"{separator*5} {title_program} {separator*5}")
number_row = int(input("How many rows to check (1-10) : "))
# Section check number row if is in range will receive for verify pass or faile.
if 1 <= number_row <= 10:
    for row_number in range(1,number_row+1):     # need start 1
        print(f"{hyphen*5} Row {row_number} {hyphen*5}")
        product_name = input("Enter product name : ").split()
        unit_price = float(input("Enter unit price (THB) : "))
        quantity = int(input("Enter quantity : "))
        # Section check data quality and if pass will calculate next then
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
        print(f"Row {row_number} : {result_row}")
    # Section display summary
    print(f"{separator*50}")
    print(f"{separator*5} {title_summary} {separator*5} ")
    print(f"{display_summary_1:<25} : {row_pass}")
    print(f"{display_summary_2:<25} : {row_fail}")
    print(f"{display_summary_3:<25} : {total:.2f}")
    print(f"{separator*50}")
else:
    print("Invalid row count: must be between 1 and 10")

