# ============================================
# File : 15_Daily_Order_Pipeline.py
# Purpose:  Turn text lines into data. Validate, summarize, compare with CRM,
#           and check your own numbers.
#           with string methods, if/elif/else, for, list, tuple, set, dict, f-string, casting
# Author: Watacharapon
# ============================================

# Variable simple data
category_names = {"STA": "Stationery", "ELC": "Electronics", "FUR": "Furniture"}
closed_customers = ("CUS-009", "CUS-010")

crm_customers = ["cus-001", "CUS-002", " cus-003 ", "CUS-004", "cus-005", "","CUS-009",]

raw_orders = [
    "ORD-3001, cus-001, STA, 10, 5.50",
    "ORD-3002,CUS-002,ELC,2,350.00",
    "ord-3003, CUS-003 ,sta,3,45.00",
    "ORD-3004,CUS-004,FUR,1,1200.00",
    "ORD-3005,CUS-777,ELC,1,99.00",
    "ORD-3002,CUS-002,ELC,2,350.00",
    "ORD-3006,CUS-001,XXX,5,10.00",
    "ORD-3007,CUS-002,ELC,0,120.00",
    "ORD-3008,CUS-005,STA,4",
    "",
    "ORD-3009,CUS-009,STA,2,10.00",
    "ABC-3010,CUS-001,STA,1,10.00",
    "ORD-3011,CUS-003,ELC,3,120.00",
    "XYZ-3012,CUS-002,ELC,1,10.00",
]

# Declaring variable
empty_lines_count = 0
count_fields = 0
seen_oder_id = set(())
reject_reasons = {}
sum_revenue_category = {}
order_category_count = {}
sum_revenue_customer = {}
count_order_customer = {}
top_revenue_category = 0
top_revenue_customer = 0
avg_category = {}
order_coverage = 0
checked_count = 0
reject_count = 0
valid_count = 0
total_in_category = 0
total_in_customer = 0
total_sum_revenue_category = 0
total_sum_revenue_customer = 0
total_in_reasons = 0

# Declearing variablr for display in report
separator = "="
hyphen = "-"
title = "Daily Order Pipeline Report"
label_raw_lines = "Raw lines"
label_empty_lines_skipped = "Empty lines skipped"
label_rows_checked = "Rows checked"
label_valid_orders = "Valid orders"
label_rejected_orders = "Rejected orders"
label_grand_total = "Grand total"
title_sales_by_category = "Sales by category"
column_1_by_category = "Category"
column_2 = "Orders"
column_3 = "Revenue"
column_4 = "Avg/order"
label_top_category = "Top category"
title_sales_by_customer = "Sales by customer"
column_1_by_customer = "Customer"
label_top_customer = "Top customer"
title_reconcile = "Customer reconciliation"
label_active_crm_customers = "Active CRM customers"
label_closed_in_crm = "Closed in CRM"
label_customers_with_orders = "Customers with orders"
label_active_but_no_orders = "Active but no orders"
label_order_coverage = "Order coverage"
title_control_checks = "Control checks"
lable_control_raw = "Raw = Empty + Checked"
lable_control_checked = "Checked = Valid + Rejected"
lable_control_category = "Category orders = Valid"
lable_control_customer = "Customer orders = Valid"
lable_control_customer = "Customer orders = Valid"
lable_control_reject =  "Reject reasons = Rejected"
lable_control_revenue = "Revenue category = customer"

# Part A Prepare reference data
# Clean crm_customers
if raw_orders != "":
    clean_crm_customers  = [customer_id.strip().upper() for customer_id in crm_customers if customer_id != "" ]
    set_crm_customer = set(clean_crm_customers)
    # casting tuple is set because Automatic Deduplication
    set_closed_customers = set(closed_customers)

    # Part B Parse and clean
    for row in raw_orders:
        row = row.strip()
        if row == "":
            empty_lines_count += 1
        else:
            reason = ""
            fields = row.split(",")
            checked_count += 1
            if len(fields) != 5:
                reason = "Row must have 5 fields"
            else:
                order_id, customer_id, category_id, qty, unit_price = fields
                clean_order_id = order_id.strip().upper()
                clean_customer_id = customer_id.strip().upper()
                clean_category_id = category_id.strip().upper()
                clean_qty = int(qty.strip())
                clean_unit_price = float(unit_price.strip())
                # Part C Validate First failure wins store reason in Dics
                if not clean_order_id.startswith("ORD-"):
                    reason = "Order ID must start with ORD-"
                elif clean_category_id not in category_names:
                    reason = "Unknown category"
                elif clean_qty <= 0:
                    reason = "Quantity must be more than 0"
                elif clean_unit_price <= 0:
                    reason = "Price must be more than 0"
                elif clean_customer_id in set_closed_customers:
                    reason = "Closed customer"
                elif clean_customer_id not in set_crm_customer:
                    reason = "Customer not in CRM"
                elif clean_order_id in seen_oder_id :
                    reason = "Duplicate order ID"
            if reason != "":
                reject_reasons[reason] = reject_reasons.get(reason, 0) + 1
                reject_count += 1
            else:
                seen_oder_id.add(clean_order_id)
                valid_count += 1
                # Part D Aggregate
                # Calculate the total amount and count orders by category
                total = clean_qty * clean_unit_price
                sum_revenue_category[clean_category_id] = sum_revenue_category.get(clean_category_id,0) + total
                order_category_count[clean_category_id] = order_category_count.get(clean_category_id,0) + 1
                # Calculate Avg/order for each category
                avg_category[clean_category_id] =  sum_revenue_category[clean_category_id]/ order_category_count[clean_category_id]

                # Calculate the total amount and count orders by customer
                sum_revenue_customer[clean_customer_id] = sum_revenue_customer.get(clean_customer_id,0) + total
                count_order_customer[clean_customer_id] = count_order_customer.get(clean_customer_id,0) + 1
    # Find Top category and Top customer
    for top_category in sum_revenue_category.values():
        if top_category > top_revenue_category:
            top_revenue_category = top_category
            top_category_id = clean_category_id
    for top_customer in sum_revenue_customer.values():
        if top_customer > top_revenue_customer:
            top_revenue_customer = top_customer
            top_customer_id = clean_customer_id
    # Part E CRM Reconcile with set operations
    set_active_crm_customers = set_crm_customer - set_closed_customers
    close_in_crm = set_crm_customer & set_closed_customers
    list_close_in_crm = list(close_in_crm)
    customers_with_orders = set(sum_revenue_customer)
    active_but_no_orders = set_active_crm_customers - customers_with_orders
    list_active_but_no_orders = list(active_but_no_orders)
    order_coverage = (len(customers_with_orders) / len(set_active_crm_customers))*100
    # Part F Control checks
    raw = "PASS" if checked_count + empty_lines_count == len(raw_orders) else "FAIL"
    checked = "PASS" if valid_count + reject_count == checked_count else "FAIL"
    for value in order_category_count.values():
        total_in_category += value
    category_orders = "PASS" if total_in_category == valid_count else "FAIL"
    for value in count_order_customer.values():
        total_in_customer += value
    customer_orders = "PASS" if total_in_customer == valid_count else "FAIL"
    for value in reject_reasons.values():
        total_in_reasons += value
    reject_reasons_count = "PASS" if total_in_reasons == reject_count else "FAIL"
    for value in sum_revenue_category.values():
        total_sum_revenue_category += value
    for value in sum_revenue_customer.values():
        total_sum_revenue_customer += value
    compair_revenue = "PASS" if total_sum_revenue_category == total_sum_revenue_customer else "FAIL"

    # Part G Display reporting
    print(f"\n{separator*5} {title} {separator*5}")
    print(f"{hyphen*50}")
    print(f"{label_raw_lines:<25} : {len(raw_orders)}")
    print(f"{label_empty_lines_skipped:<25} : {empty_lines_count}")
    print(f"{label_rows_checked:<25} : {checked_count}")
    print(f"{label_valid_orders:<25} : {valid_count}")
    print(f"{label_rejected_orders:<25} : {reject_count}")
    print(f"{label_rejected_orders:<25} : {total_sum_revenue_customer:.2f}")
    print(f"{hyphen*50}")
    if valid_count > 0:
        print(title_sales_by_category)
        print(f"{column_1_by_category:<15} | {column_2:<10} | {column_3:<10} | {column_4}")
        for key in category_names.keys():
            print(f"{category_names.get(key):<15} | {order_category_count.get(key):<10} | {sum_revenue_category.get(key):<10} | {avg_category.get(key)}")
        print(f"{label_top_category:<25} : {category_names.get(top_category_id)} ({top_revenue_category})")
        print(f"{hyphen*50}")
        print(title_sales_by_customer)
        print(f"{column_1_by_customer:<15} | {column_2:<10} | {column_3:<10}")
        for key in sum_revenue_customer.keys():
            print(f"{key:<15} | {count_order_customer.get(key):<10} | {sum_revenue_customer.get(key)} ")
        print(f"{label_top_customer:<25} : {top_customer_id} ({top_revenue_customer:.2f})")
    else:
        print("No valid orders found")
    print(f"{hyphen*50}")
    print(f"{title_reconcile}")
    print(f"{label_active_crm_customers:<25} : {len(set_active_crm_customers)}")
    print(f"{label_closed_in_crm:<25} : {list_close_in_crm}")
    print(f"{label_customers_with_orders:<25} : {len(customers_with_orders)}")
    print(f"{label_active_but_no_orders:<25} : {list_active_but_no_orders}")
    print(f"{label_order_coverage:<25} : {order_coverage}%")
    print(f"{hyphen*50}")
    if reject_count > 0:
        for reason, count in reject_reasons.items():
            print(f"{reason:<35} : {count}")
    else:
        print("No rejected orders")
    print(f"{hyphen*50}")
    print(f"{title_control_checks}")
    print(f"{lable_control_raw:<30} : {raw}")
    print(f"{lable_control_checked:<30} : {checked}")
    print(f"{lable_control_category:<30} : {category_orders}")
    print(f"{lable_control_category:<30} : {customer_orders}")
    print(f"{lable_control_reject:<30} : {reject_reasons_count}")
    print(f"{lable_control_revenue:<30} : {compair_revenue}")
else:
    print("No orders to check")