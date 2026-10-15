# ============================================
# File : 11_Order_ID_Batch_Cleaner.py
# Purpose:  Practice Order IDs from two stores are messy. 
#           with list + string methods + loop
#           Build a script that cleans IDs from two stores 
#           and prints a summary report.
# Author: Watacharapon
# ============================================

# Declaring variable
clean_order_id = []
not_empty_order_id = []
correct_order_id = []
incorrect_order_id = []
count_remove = 0
remove_duplicate_order_id = []
sort_order_id=[]
first_id = ""
last_id = ""

# variable for display
separator = "="
hyphen = "-"
title_summary = "Order ID Batch Report"
display_1 = "Rows read"
display_2 = "Empty skipped"
display_3 = "Invalid IDs"
display_4 = "Duplicates removed"
display_5 = "Valid unique IDs"
display_6 = "Sorted IDs"
display_7 = "First ID"
display_8 = "Last ID"

# Input by store value original 
order_id_store_a = input("Store A Enter Order ID : ")
order_id_store_b = input("Store B Enter Order ID : ")

# Section cleanning before validate become report
# split value from comma and store is data type list
split_order_id_store_a = order_id_store_a.split(",")
split_order_id_store_b = order_id_store_b.split(",")
order_id = split_order_id_store_a+split_order_id_store_b

# Section cleaning
for item in order_id:
    clean_order_id.append(item.upper().strip())

# Section check valid
# Skip empty values and count them.
count_empty_values = clean_order_id.count("")
for item in clean_order_id:
    if item != "":
        not_empty_order_id.append(item)
# A valid ID must start with ORD-. Keep invalid IDs in a separate list.
for item in not_empty_order_id:
    if str(item).startswith("ORD-"):
        correct_order_id.append(item)
    else:
        incorrect_order_id.append(item)
if len(correct_order_id) > 0:
    # Remove duplicates. Keep the first one. Count how many were removed.
    for item in correct_order_id:
        remove_duplicate_order_id.append(item)
        if remove_duplicate_order_id.count(item) > 1:
            count_remove +=1
            remove_duplicate_order_id.remove(item)
    # Sort IDs from small to large.
    for item in remove_duplicate_order_id:
        sort_order_id.append(item)
        sort_order_id.sort()
    first_id = sort_order_id[0]
    last_id = sort_order_id[-1]
            
    # Display output result to make it easy to read
    if len(sort_order_id) == 1:
        print(f"{display_5:<25} : {len(sort_order_id)}")
        print(f"{display_4:<25} : {count_remove}")
    else:
        print(f"\n{separator*5} {title_summary} {separator*5}")
        print(hyphen*50)
        print(f"{display_1:<25} : {len(order_id)}")
        print(f"{display_2:<25} : {count_empty_values}")
        print(f"{display_3:<25} : {len(incorrect_order_id)} => {incorrect_order_id}")
        print(f"{display_4:<25} : {count_remove}")
        print(f"{display_5:<25} : {len(sort_order_id)}")
        print(f"{display_6:<25} : {sort_order_id}")
        print(f"{display_7:<25} : {first_id}")
        print(f"{display_8:<25} : {last_id}")
        print(hyphen*50)
else:
    print("No valid ID found")