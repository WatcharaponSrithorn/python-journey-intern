# ============================================
# File : 06_Customer_Tier_Classifier.py
# Purpose:  Practice using if, else, elif , Nested if , 
#           classify data into categories based on multiple layered conditions
# Author: Watacharapon
# ============================================

# declaring varible 
tier = ""           
reason = ""
separator = "="
title_program = "Customer Tier Classification"
title_result = "CUSTOMER TIER RESULT"
display_1 = "Tier"
display_2 = "Reason"


# Input value for check conditions must specify data type
print(f"{separator*5} {title_program} {separator*5}")       # display title program
print("-"*50)
print(" ")
total_spending = float(input("Enter total spending (THB) : "))  # input() always returns a string, so cast to float for math and inform and Specify the currency protect
membership_years = int(input("Enter member year amount : "))    # input() always returns a string, so cast to int for math
has_complaint = input("Any complaint history? (yes/no) :")


# Process Classify the tier
if total_spending >= 100000:
    if membership_years >= 3:
        if has_complaint == "no" or has_complaint == "No":
            tier = "Platinum"
            reason = f"High spending {total_spending}, member {membership_years} year, {has_complaint} has complaint "
        else:
            tier = "Gold"
            reason = f"High spending {total_spending}, member {membership_years} year, But has complaint {has_complaint}"
    else:
        tier = "Gold"
        reason = f"High spending {total_spending},member {membership_years} year less than 3 year"
elif total_spending >= 30000:
    if membership_years >= 1:
        tier = "Silver"
        reason = f"low spending {total_spending} less than 100,000 , member {membership_years} year more than 1 year"
    else:
        tier = "Bronze"
        reason = f"low spending {total_spending} less than 100,000 but more than 30,000 , But  member {membership_years} year less than 1 year"
else:
    tier = "Bronze"
    reason = f"low spending {total_spending} less than 30,000  "


# Output result tier and reason from Classify
print(" ")
print(f"{separator*50}")
print(f"{title_result:^50}")
print(f"{separator*50}")
print(f"{display_1:<15} :  {tier}")
print(f"{display_2:<15} :  {reason}")
print(f"{separator*50}")