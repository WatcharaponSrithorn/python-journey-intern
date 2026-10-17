# ============================================
# File : 12_Sales_Row_Tuple_Validator.py
# Purpose:  Sales data comes as rows. Some rows are bad. 
#           Check each row and tell us why it is rejected.
#           with tuple + list + string methods + loop + if..else
# Author: Watacharapon
# ============================================

# Varible received form Sales
rows = [
    ("ORD-1001", "Pen", 10, 5.50),
    ("ORD-1002", "Notebook", 3, 45.00),
    ("ORD-1003", "Stapler", 0, 120.00),
    ("ABC-1004", "Ruler", 5, 12.00),
    ("ORD-1005", "Marker", 4),
    ("ORD-1002", "Notebook", 3, 45.00),
    ("ORD-1006", "Folder", 20, -2.50),
    ("ORD-1007", "Calculator", 2, 350.00),
]

# variable 
list_reject = []
valid_rows = []
not_duplicate_id = []
grand_total = 0
list_total = []
top_total = 0
top_order = []
# varible for display
separator = "="
hyphen = "-"
title_summary = "Sales Row Validation Report"
label_total_rows = "Total rows"
label_valid_rows = "Valid rows"
label_rejected_rows = "Rejected rows"
label_grand_total = "Grand total"
label_top_order = "Top order"
title_valid_orders = "Valid orders (sorted by Order ID)"
title_rejected = "Rejected rows"


# Loop through each row and get the row number
if rows != []:
    for index, item  in enumerate(rows, start=1):
        reason_reject =""
        if len(item) != 4:
            reason_reject = "Row must have 4 items"
        else:
            order_id, product, quantity, unit_price = item
            if not order_id.startswith("ORD-"):
                reason_reject = "Order ID must start with ORD-"
            elif quantity <= 0:
                reason_reject = "Quantity must be more than 0"
            elif unit_price <= 0:
                reason_reject = "Price must be more than 0"
            elif order_id in not_duplicate_id :
                reason_reject = "Duplicate order ID"
            elif order_id not in not_duplicate_id:
                not_duplicate_id.append(order_id)
        if reason_reject != "":
            list_reject.append(f"Row {index} | {order_id} | {reason_reject}")
        else:
            total = quantity * unit_price
            tuple_valid_rows = tuple((order_id,product,quantity,unit_price,total))
            valid_rows.append(tuple_valid_rows)
            grand_total += total
            list_total.append(total)
    top_order.append(order_id)
    for item in list_total:
        if item > top_total:
            top_total = item
            top_order.append(order_id)
            reject_top = top_order.pop(0)

    print(f"{separator*5} {title_summary} {separator*5}")
    print(hyphen*50)
    print(f"{label_total_rows:<25} : {index}")
    print(f"{label_valid_rows:<25} : {len(valid_rows)}")
    print(f"{label_rejected_rows:<25} : {len(list_reject)}")
    print(f"{label_grand_total:<25} : {grand_total}")
    print(f"{label_top_order:<25} : {top_order} {top_total}")
    print(hyphen*50)
    print(title_valid_orders)
    if valid_rows != []: 
        for item in valid_rows:
            order_id, product, quantity, unit_price, total = item
            print(f"{order_id:<10} | {product:<10} | {quantity:<5} | {unit_price:<10.2f} | {total:.2f}")
    else:
        print("No valid orders found")
    print(hyphen*50)
    print(title_rejected)
    for item in list_reject:
        print(item)
    print(hyphen*50)
else:
    print("No rows to check")