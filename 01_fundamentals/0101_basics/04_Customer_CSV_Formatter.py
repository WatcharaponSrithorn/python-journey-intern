# ============================================
# File : 04_Customer_CSV_Formatter.py
# Purpose: Collect customer data and display one CSV row
# Author: Watacharapon
# ============================================

print("CUSTOMER DATA TO CSV ROW FORMATTER")
print("Enter customer data without commas.")

# Input
customer_id = input("Enter customer ID : ")
while "," in customer_id:
    print("Commas are not allowed. Please enter the customer ID again.")
    customer_id = input("Enter customer ID : ")

full_name = input("Enter full name : ")
while "," in full_name:
    print("Commas are not allowed. Please enter the full name again.")
    full_name = input("Enter full name : ")

age = input("Enter age : ")
while "," in age:
    print("Commas are not allowed. Please enter the age again.")
    age = input("Enter age : ")

membership_fee = input("Enter membership fee : ")
while "," in membership_fee:
    print("Commas are not allowed. Please enter the membership fee again.")
    membership_fee = input("Enter membership fee : ")

is_active = input("Is the customer active? (True/False) : ")
while "," in is_active:
    print("Commas are not allowed. Please enter the active status again.")
    is_active = input("Is the customer active? (True/False) : ")

signup_year = input("Enter signup year : ")
while "," in signup_year:
    print("Commas are not allowed. Please enter the signup year again.")
    signup_year = input("Enter signup year : ")

# Process
csv_header = "customer_id,full_name,age,membership_fee,is_active,signup_year"
csv_row = f"{customer_id},{full_name},{age},{membership_fee},{is_active},{signup_year}"

# Output
print()
print("Header + Data")
print(csv_header)
print(csv_row)

print()
print("Readable Summary")
print(f"Customer ID : {customer_id}")
print(f"Full Name : {full_name}")
print(f"Age : {age}")
# Keep the original membership_fee string in the CSV row; round only for display.
print(f"Membership Fee : {float(membership_fee):.2f}")
print(f"Is Active : {is_active}")
print(f"Signup Year : {signup_year}")
