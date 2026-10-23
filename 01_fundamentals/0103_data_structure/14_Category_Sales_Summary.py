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
column_category = "Category"
column_order = "Orders"
column_revenue = "Revenue"
column_avg = "Avg/order"
title_reason = "Rejected reasons"

# Section check the row size before unpack.
for row in rows:
    reason = ""
    if len(row) != 4:
        reason = "Row must have 4 items"
    else:
        # clean category_id after unpack
        order_id, category_id, qty, unit_price = row
        clean_category_id = category_id.upper().strip()
        # check validate Unknown category in category_names
        if clean_category_id not in category_names:
            reason = "Unknown category"
        # check validate Quantity must be more than 0
        elif qty <= 0:
            reason = "Quantity must be more than 0"
        # check validate Price must be more than 0
        elif unit_price <= 0:
            reason = "Price must be more than 0"
    # Row valid calculate total store revenue_by_category and orders_by_category
    # store values valid row, grand total and if != "" store reject row
    if reason == "":
        total = qty * unit_price
        grand_total += total
        revenue_by_category[clean_category_id] = revenue_by_category.get(clean_category_id, 0) + total
        orders_by_category[clean_category_id] = orders_by_category.get(clean_category_id, 0) + 1
        valid_rows += 1
    else:
        reject_reasons[reason] = reject_reasons.get(reason, 0) + 1
        reject_rows += 1
# Section find Top category
for category_code, revenue in revenue_by_category.items():
    if revenue > top_revenue:
        top_revenue = revenue
        top_category = category_code
    # Section calculate Avg/order
    avg_order[category_code] = revenue / orders_by_category[category_code]

# Section display report
if len(rows) != 0:
    print(f"\n{separator*5} {title_report} {separator*5}")
    print(hyphen*50)
    print(f"{label_total_rows:<20} : {len(rows)}")
    print(f"{label_valid_rows:<20} : {valid_rows}")
    print(f"{label_rejected_rows:<20} : {reject_rows}")
    print(f"{label_grand_total:<20} : {grand_total:.2f}")
    if valid_rows != 0:
        print(f"{label_top_category:<20} : {category_names.get(top_category)} ({top_revenue:.2f})")
        print(hyphen*50)
        print(f"{column_category:<20} | {column_order:<6} | {column_revenue:<10} | {column_avg}")
        for key in revenue_by_category:
            print(f"{category_names[key]:<20} | {orders_by_category[key]:<6} | {revenue_by_category[key]:<10.2f} | {avg_order[key]:.2f}")
    else:
        print(hyphen*50)
        print("No valid orders found")
    print(hyphen*50)
    print(title_reason)
    if len(reject_reasons) != 0:
        for reject_reason, reject_count in reject_reasons.items():
            print(f"{reject_reason:<30} : {reject_count}")
    else:
        print("No rejected rows")
    print(hyphen*50)
else:
    print("No rows to check")
