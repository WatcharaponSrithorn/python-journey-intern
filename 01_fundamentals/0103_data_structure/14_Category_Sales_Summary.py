# ============================================
# File : 14_Category_Sales_Summary.py
# Purpose:  Group sales by category. Count why rows are rejected.
#           with Dictionary
# Author: Watacharapon
# ============================================

# Variable sample data
category_names = {"STA": "Stationery", "ELC": "Electronics", "FUR": "Furniture"}

rows = [
    ("ORD-2001", "STA", 10, 5.50),
    ("ORD-2002", "ELC", 2, 350.00),
    ("ORD-2003", "STA", 3, 45.00),
    ("ORD-2004", "FUR", 1, 1200.00),
    ("ORD-2005", "ELC", 0, 99.00),
    ("ORD-2006", "XXX", 5, 10.00),
    ("ORD-2007", "STA", 4),
    ("ORD-2008", "ELC", 1, 350.00),
    ("ORD-2009", "STA", 6, -1.00),
    ("ORD-2010", "ELC", 3, 120.00),
    ("ORD-2011", " sta ", 2, 10.00),
]

# Declaring variable
revenue_by_category = {}
orders_by_category = {}
reject_reasons = {}
avg_order = {}
top_revenue = 0
valid_rows = 0
reject_rows = 0
grand_total = 0

# variable for display
separator = "="
hyphen = "-"
title_report = "Category Sales Summary"
label_total_rows = "Total rows"
label_valid_rows = "Valid rows"
label_rejected_rows = "Rejected rows"
label_grand_total = "Grand total"
label_top_category = "Top category"
column_category = "Category "
column_order = "Orders"
column_revenue = "Revenue"
column_avg = "Avg/order"
title_reason = "Rejected reasons"

# Secsion check the row size before unpack.
for row, item in enumerate(rows,start=1):
    reason = ""
    if len(item) != 4:
        reason = "Row must have 4 items"
        reject_reasons[reason] = reject_reasons.get(reason,0) +1
    else:
        # clean category_id after unpack
        order_id, category_id, qty, unit_price = item
        clean_category_id = category_id.upper().strip()
        # check validate Unknown category in category_names
        key_category = category_names.keys()
        if clean_category_id not in key_category:
            reason = "Unknown category"
            reject_reasons[reason] = reject_reasons.get(reason,0) +1
        # check validate Quantity must be more than 0
        elif qty <= 0:
            reason = "Quantity must be more than 0"
            reject_reasons[reason] = reject_reasons.get(reason,0) +1
        # check validate Price must be more than 0
        elif unit_price <= 0:
            reason = "Price must be more than 0"
            reject_reasons[reason] = reject_reasons.get(reason,0) +1
        # Row valid calaulate total store revenue_by_category and orders_by_category
        else:
            total = qty * unit_price
            revenue_by_category[clean_category_id] = revenue_by_category.get(clean_category_id,0) + total
            orders_by_category[clean_category_id] = orders_by_category.get(clean_category_id,0) + 1

# Section find Top category
for item in revenue_by_category.items():
    category_id, revenue = item
    if revenue > top_revenue:
        top_revenue = revenue
        top_category = category_id
    # Section calculate Avg/order
    avg_order[category_id] = revenue / orders_by_category[category_id]

# Section display report
if len(rows) != 0:
    print(f"\n{separator*5} {title_report} {separator*5}")
    print(hyphen*50)
    print(f"{label_total_rows:<20} : {len(rows)}")
    # Find value of valid rows
    for item in orders_by_category.values():
        valid_rows += item
    print(f"{label_valid_rows:<20} : {valid_rows}")
    # Find value of Rejected rows
    for item in reject_reasons.values():
        reject_rows += item
    print(f"{label_rejected_rows:<20} : {reject_rows}")
    # Find value of Grand total
    for item in revenue_by_category.values():
        grand_total += item
    print(f"{label_grand_total:<20} : {grand_total:.2f}")
    if valid_rows != 0:
        print(f"{label_top_category:<20} : {category_names.get(top_category)} ({top_revenue:.2f})")
        print(hyphen*50)
        print(f"{column_category:<20} | {column_order:<6} | {column_revenue:<10} | {column_avg}")
        print(f"{category_names.get('STA'):<20} | {orders_by_category.get('STA'):<6} | {revenue_by_category.get('STA'):<10.2f} | {avg_order.get('STA'):.2f} ")
        print(f"{category_names.get('ELC'):<20} | {orders_by_category.get('ELC'):<6} | {revenue_by_category.get('ELC'):<10.2f} | {avg_order.get('ELC'):.2f} ")
        print(f"{category_names.get('FUR'):<20} | {orders_by_category.get('FUR'):<6} | {revenue_by_category.get('FUR'):<10.2f} | {avg_order.get('FUR'):.2f} ")
    else:
        print(hyphen*50)
        print("No valid orders found")
    print(hyphen*50)
    print(title_reason)
    if len(reject_reasons) != 0:
        for item in reject_reasons.items():
            reason, amount = item
            print(f"{reason:<30} : {amount}")
    else:
        print(reject_reasons)
else:
    print("No rows to check")