# ============================================
# File : 11_Order_ID_Batch_Cleaner.py
# Purpose:  Clean Order IDs from two stores and print a summary report.
#           with list + string methods + loop + if..else
# Author: Watacharapon
# ============================================

# Declaring variable
non_empty_ids = []
valid_ids = []
invalid_ids = []
count_remove = 0
unique_ids = []

# variable for display
separator = "="
hyphen = "-"
title_summary = "Order ID Batch Report"
label_rows_read = "Rows read"
label_empty = "Empty skipped"
label_invalid = "Invalid IDs"
label_duplicates = "Duplicates removed"
label_unique = "Valid unique IDs"
label_sorted = "Sorted IDs"
label_first = "First ID"
label_last = "Last ID"

# Input by store value original 
order_id_store_a = input("Store A Enter Order ID : ")
order_id_store_b = input("Store B Enter Order ID : ")

# Section cleaning before validate become report
# split value from comma and store is data type list
split_order_id_store_a = order_id_store_a.split(",")
split_order_id_store_b = order_id_store_b.split(",")
order_id = split_order_id_store_a + split_order_id_store_b
clean_ids = [item.upper().strip() for item in order_id]

# Section check valid
# Skip empty values and count them.
count_empty_values = clean_ids.count("")
for item in clean_ids:
    if item != "":
        non_empty_ids.append(item)
# A valid ID must start with ORD-. Keep invalid IDs in a separate list.
for item in non_empty_ids:
    if item.startswith("ORD-"):
        valid_ids.append(item)
    else:
        invalid_ids.append(item)
if len(valid_ids) > 0:
    # Remove duplicates. Keep the first one. Count how many were removed.
    for item in valid_ids:
        if item in unique_ids:
            count_remove += 1
        else:
            unique_ids.append(item)

    # Sort IDs from small to large.
    unique_ids.sort()
    first_id = unique_ids[0]
    last_id = unique_ids[-1]
            
    # Display output result to make it easy to read
    print(f"\n{separator*5} {title_summary} {separator*5}")
    print(hyphen*50)
    print(f"{label_rows_read:<25} : {len(order_id)}")
    print(f"{label_empty:<25} : {count_empty_values}")
    print(f"{label_invalid:<25} : {len(invalid_ids)} => {invalid_ids}")
    print(f"{label_duplicates:<25} : {count_remove}")
    print(f"{label_unique:<25} : {len(unique_ids)}")
    print(f"{label_sorted:<25} : {unique_ids}")
    print(f"{label_first:<25} : {first_id}")
    print(f"{label_last:<25} : {last_id}")
    print(hyphen*50)
else:
    print("No valid ID found")