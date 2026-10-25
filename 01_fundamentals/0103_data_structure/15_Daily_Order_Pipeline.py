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

# Part A Prepare reference data
# Clean crm_customers
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
        else:
            seen_oder_id.add(clean_order_id)
            # Part D Aggregate
            # Calculate the total amount and count orders by category
            total = clean_qty * clean_unit_price
            sum_revenue_category[clean_category_id] = sum_revenue_category.get(clean_category_id,0) + total
            order_category_count[clean_category_id] = order_category_count.get(clean_category_id,0) + 1

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
            # Calculate Avg/order for each category
            avg_category[clean_category_id] =  sum_revenue_category[clean_category_id]/ order_category_count[clean_category_id]