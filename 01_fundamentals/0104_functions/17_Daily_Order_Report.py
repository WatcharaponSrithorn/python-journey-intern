# ============================================
# File    : 17_Daily_Order_Report.py
# Purpose : TPrint a daily order report. Clean names, check quantity,
#           and calculate totals with return functions.
# Concepts: Function with return, *args,  def, parameter, default parameter, for loop
# Issue   : #38
# Author  : Watacharapon
# Date    : 2026-11-09
# ============================================

MIN_QUANTITY = 1
# Main data (order_id, raw_name, quantity, unit_price)
orders = [
    ("ORD-001", "  somchai  ", 2, 50.00),
    ("ORD-002", "MALI", 1, 120.50),
    ("ORD-003", "   ", 3, 30.00),
    ("ORD-004", "john", 0, 45.00),
    ("ORD-005", "  lisa", 4, 25.00),
]

# Part A Create function and return
# Function Print a title with lines **additional
def printTitle(title, symbol="="):
    print(symbol*30)
    print(title)
    print(symbol*30)


# Function for clean raw_name
def cleanName(raw_name, default="UNKNOWN"):
    clean_name = raw_name.strip().upper()
    if clean_name == "":
        return default
    else:
        return clean_name


# Function for check quantity must not be less than MIN_QUANTITY
def isValidQuantity(quantity, min_quantity=MIN_QUANTITY):
    if quantity >= min_quantity:
        return True
    else:
        return False


# Function for calculate amount of each order_id
def calculateTotal(quantity, unit_price):
    total = quantity * unit_price
    return total


# Function for sum of function calculateTotal
def addAll(*totals):
    sum_total = 0
    for i in totals:
        sum_total += i
    return sum_total


# Part B Use function in loop
if len(orders) > 0:
    count_reject = 0
    count_valid = 0
    list_total = []
    printTitle("DAILY ORDER REPORT")
    for order_id, raw_name, quantity, unit_price in orders:
        if isValidQuantity(quantity):
            total = calculateTotal(quantity, unit_price)
            print(f"[{order_id}] {cleanName(raw_name)} | total {total:.2f}")
            list_total.append(total)
            count_valid += 1
        else:
            print(f"[{order_id}] REJECTED | Quantity must be at least {MIN_QUANTITY}")
            count_reject += 1
    print("-"*30)

    # Part C Summary
    print(f"Valid orders    : {count_valid}")
    print(f"Rejected orders : {count_reject}")
    print(f"Grand total     : {addAll(*list_total):.2f}")
    if count_valid + count_reject == len(orders):
        control_result = "PASS"
    else:
        control_result = "FAIL"
    print(f"Control check   : {control_result}")
    print("-"*30)
else:
    print("No orders to check")
# Part D test default value and edge case
result = isValidQuantity(2, min_quantity=3)
print(f"[TEST] quantity 2, min 3 -> {result}")