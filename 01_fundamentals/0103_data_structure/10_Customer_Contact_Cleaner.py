# ============================================
# File : 10_Customer_Contact_Cleaner.py
# Purpose:  Practice cleaning and validating text with string methods, input, if/elif/else
#           clean one raw record and check its 
#           format using string methods.
# Author: Watacharapon
# ============================================

# Declaring variable 
clean_name = ""             # stores the cleaned name, built word by word in the loop
result_check_phone = ""     # for store result checking phone
result_check_email = ""     # for store result checking Email
format_phone = ""
result_overall = ""
is_valid = False
user_name = ""
clean_email = ""
clean_phone = ""
user_name = ""

# variable for display
separator = "="
hyphen = "-"
title_program = "Customer Contact Cleaner"
display_error = "Name must have first and last name"
title_summary = "CLEAN RESULT"
display_1 = "Name   (before)"
display_2 = "Name   (after)"
display_3 = "Email  (before)"
display_4 = "Email  (after)"
display_5 = "Phone  (before)"
display_6 = "Phone  (after)"
display_7 = "Email check"
display_8 = "Phone check"
display_9 = "Email username"
display_10 = "Phone display"
display_11 = "Overall"

# Section input user for 3 raw values
print(f"{separator*5} {title_program} {separator*5}")
raw_name = input("Enter your name : ")
raw_email = input("Enter your E-mail : ")
raw_phone = input("Enter your Mobile Phone : ")

# Section Clean BEFORE validate.
# Why: validation rules are strict (exact length, endswith ".com").
# Raw input often has extra spaces, capital letters, or dashes, e.g.
# " Somchai@Mail.COM " or "081-234-5678". If we validate the raw value,
# .endswith(".com") fails because of the trailing space and capital "COM",
# and len() counts the dashes, so we would reject perfectly good data.

# cleaning name 
# Why split() first: split() without arguments ignores extra spaces,
# so "  somchai   jaidee " still gives exactly 2 words for the
# first-name/last-name check.
# capitalize the first letter
name = raw_name.split()
if len(name) == 2 :
    # index first string capitalize
    for i in name:
        clean_name += i[0:1].upper() + i[1:].lower() + " "
    # Remove withespace
    clean_name = clean_name.strip(" ")

    # cleaning E-mail 
    # Why strip + lower: users type spaces and capitals by accident.
    # Emails are not case-sensitive, so lowercase gives one consistent form
    # and lets .endswith(".com") work reliably.
    clean_email = raw_email.strip().lower()
    
    # cleaning phone number 
    # Why remove "-": users type 081-234-5678, but the rule checks for
    # exactly 10 digits. Without removing dashes, len() would be 12 and
    # a valid number would FAIL.
    clean_phone = raw_phone.strip().replace("-","")

    # Section validate
    # check phone number
    if len(clean_phone) != 10:
        result_check_phone = "FAIL: must be 10 digits"
    elif clean_phone.startswith("0") == False:
        result_check_phone = "FAIL: must start with 0"
    else:
        result_check_phone = "PASS"
    # Check E-mail
    if clean_email.count("@") != 1:
        result_check_email = "FAIL: must have exactly one @"
    elif clean_email.endswith(".com") == False:
        result_check_email = "FAIL: must end with .com only"
    elif clean_email.find("@") == 0:
        result_check_email = "FAIL: No username before @"
    else:
        result_check_email = "PASS"

    # Section Extract the username from the part of the email address before @.
    if result_check_email == "PASS":
        position_2 = clean_email.find("@")
        user_name = clean_email[:position_2]

    # Section format output clean_phone xxx-xxx-xxxx if PASS
    if result_check_phone == "PASS":
        format_phone = clean_phone[0:3]+hyphen+clean_phone[3:6]+hyphen+clean_phone[6:]
    else:
        format_phone = "Cannot format the data phone"

    # Section check Overall
    if result_check_email != "PASS":
        result_overall = "FAIL - Do not save"
    elif result_check_phone != "PASS":
        result_overall = "FAIL - Do not save"
    else:
        result_overall = "PASS - Ready to save"
        is_valid = True

    # Display output result to make it easy to read
    print(separator*50)
    print(f"{title_summary:^50}")
    print(separator*50)
    print(f"{display_1:<22} : {raw_name}")
    print(f"{display_2:<22} : {clean_name}")
    print(f"{display_3:<22} : {raw_email}")
    print(f"{display_4:<22} : {clean_email}")
    print(f"{display_5:<22} : {raw_phone}")
    print(f"{display_6:<22} : {clean_phone}")
    print(hyphen*50)
    print(f"{display_7:<22} : {result_check_email}")
    print(f"{display_8:<22} : {result_check_phone}")
    print(hyphen*50)
    # Why check email and phone separately first: we only show username and
    # formatted phone when data is valid, so we never display half-bad data.
    if is_valid == True:
        print(f"{display_9:<22} : {user_name}")
        print(f"{display_10:<22} : {format_phone}")
    print(f"{display_11:<22} : {result_overall}")
    print(hyphen*50)
else:
    print(display_error)