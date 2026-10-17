# ============================================
# File : 12_Sales_Row_Tuple_Validator.py
# Purpose:  Sales data comes as rows. Some rows are bad.
#           Check each row and tell us why it is rejected.
#           with tuple + list + string methods + loop + if..else
# Author: Watacharapon
# ============================================

# Variable received from Sales
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
rejected_rows = []
valid_rows = []
seen_ids = []
grand_total = 0
top_total = 0
top_order = ""
# variable for display
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
    for index, item in enumerate(rows, start=1):
        reason_reject = ""
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
            elif order_id in seen_ids:
                reason_reject = "Duplicate order ID"
        if reason_reject != "":
            rejected_rows.append((index, item[0], reason_reject))
        else:
            seen_ids.append(order_id)
            total = quantity * unit_price
            tuple_valid_row = item + (total,)
            valid_rows.append(tuple_valid_row)
            grand_total += total
    for item in valid_rows:
        order_id, product, quantity, unit_price, total = item
        if total > top_total:
            top_total = total
            top_order = order_id

    print(f"{separator*5} {title_summary} {separator*5}")
    print(hyphen*50)
    print(f"{label_total_rows:<25} : {len(rows)}")
    print(f"{label_valid_rows:<25} : {len(valid_rows)}")
    print(f"{label_rejected_rows:<25} : {len(rejected_rows)}")
    print(f"{label_grand_total:<25} : {grand_total:.2f}")
    if len(valid_rows) != 0:
        print(f"{label_top_order:<25} : {top_order} ({top_total:.2f})")
    print(hyphen*50)
    print(title_valid_orders)
    valid_rows.sort()
    if valid_rows != []:
        for item in valid_rows:
            order_id, product, quantity, unit_price, total = item
            print(f"{order_id:<10} | {product:<10} | {quantity:<5} | {unit_price:<10.2f} | {total:.2f}")
    else:
        print("No valid orders found")
    print(hyphen*50)
    print(title_rejected)
    for item in rejected_rows:
        index, order_id, reason_reject = item
        print(f"Row {index} | {order_id} | {reason_reject}")
    print(hyphen*50)
else:
    print("No rows to check")