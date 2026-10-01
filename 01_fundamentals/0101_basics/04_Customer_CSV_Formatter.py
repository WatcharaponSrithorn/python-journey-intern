# ============================================
# File : 04_Customer_CSV_Formatter.py
# Purpose:  Practice logical about Data Engineer's job
# Author: Watacharapon
# ============================================

# Declaring variable
tiltel_entry = "Customer Data Entry"
csv_raw = "CSV Row (raw, for system ingestion)"
header_data ="customer_id,full_name,age,membership_fee,is_active,signup_year"
text_summary = "Readable Summary"
tiltel_summary = "CUSTOMER SUMMARY"
display_1 = "Customer ID"
display_2 = "Full Name"
display_3 = "Age"
display_4 = "Membership Fee"
display_5 = "Active Status"
display_6 = "Signup Year"

# Input
print(f"{"="*5} {tiltel_entry} {"="*5}")
customer_id = input("Enter customer ID : ")
full_name = input("Enter full name of customer  : ")
age = int(input("Enter age of customer : "))                # input() always returns string, so cast to int for math
membership_fee = float(input("Enter membership fee of customer : ")) # input() always returns string, so cast to Float for math because is finance
is_active = input("Is the customer active? (True/False): only : ")      
signup_year = int(input("Enter year register : "))          # input() always returns string, so cast to int for math

# Section: Comma Check
has_comma = "," in full_name        # in checks if something inside with strings
print(" ")                          # for Leave a blank line.
print(f"Comma check in full name -> False = No have , True = Have ? -> {has_comma}") # True if have comma, False if have not

# Output
# Section: Display CSV Row
print(" ")                          # for Leave a blank line.
print(f"{"="*5} {csv_raw} {"="*5}")
print(header_data)
print(f"{customer_id},{full_name},{age},{membership_fee},{is_active},{signup_year}")
                                        # don't round numbers  keep the original precision.

# Section: Display Readable Summary
print(" ")                          # for Leave a blank line.
print(f"{"="*5} {text_summary} {"="*5}")
print("="*50)
print(f"{tiltel_summary:^50}")                      # :^50 centers the text in a 50-character width
print("="*50)
print(f"{display_1:<25}: {customer_id}")
print(f"{display_2:<25}: {full_name}")
print(f"{display_3:<25}: {age}")
print(f"{display_4:<25}: {membership_fee:.2f}")     # use .2f Rounding is only for display
print(f"{display_5:<25}: {is_active}")
print(f"{display_6:<25}: {signup_year}")