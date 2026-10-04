# ============================================
# File : 05_Customer_Data_Validator.py
# Purpose:  Practice using if, else, elif by data must be checked 
#           for quality BEFORE it enters the system
# Author: Watacharapon
# ============================================

# section input
age = int(input("Enter age : "))        # input() alway String, so cast to int for math and data quality
membership_fee = int(input("Enter membership fee (THB) : ")) # input() alway String, so cast to int for math and inform and Specify the currency protect 
is_active = input("Is the customer active? (True / False ) : ")
email = input("Enter email : ")

# declaring variable for store result about validation value
result_age = ""
result_membership_fee = ""
result_is_active = ""
result_email = ""
result_summary = ""
# declaring variable for display
separator = "="
title_report = "Validation Result"
display_1 = "Age"
display_2 = "Membership fee"
display_3 = "Is active"
display_4 = "Email"
title_result = "Overall Result"

# section validation value to input
# section about age betwwen 18-100 only
if age <= 18:
    result_age = "Age too young (must be 18+)"
elif age >100:
    result_age = "Age invalid (too high)"
else:
    result_age = "OK"

# section about membership_fee for 0 will calculate error 0 * Anyway = 0 
result_membership_fee = "Membership fee invalid (must be more than 0)" if membership_fee <= 0 else "OK"

# section about is_active will store value is Boolean allow first word starts both lower or upper
result_is_active = "OK" if (is_active == "True" or is_active == "true") or (is_active == "False" or is_active == "false") else "Active status invalid (must be true or false)"

# section about email validation user enter email must put @
result_email = "OK" if "@" in email else "Email invalid (missing @)"

# section about validation summary "Is this data ready to save?"
# by change data type is Bool
bool_age = True if result_age =="OK" else False
bool_membership_fee = True if result_membership_fee =="OK" else False
bool_is_active = True if result_is_active =="OK" else False
bool_email = True if result_email =="OK" else False

# summary result of vaidation value
if bool_age and bool_membership_fee and bool_is_active and bool_email:
    result_summary = "PASS - Ready to save"
else:
    result_summary = "FAIL - Do not save"

# Output Validation Result
print(" ")                              # for Leave a blank line.
print(f"{separator*5} {title_report} {separator*5}")
print("="*50)
print(f"{display_1:<25} : {result_age}")
print(f"{display_2:<25} : {result_membership_fee}")
print(f"{display_3:<25} : {result_is_active}")
print(f"{display_4:<25} : {result_email}")
print("-"*50)
print(f"{title_result:<25} : {result_summary}")
print("="*50)