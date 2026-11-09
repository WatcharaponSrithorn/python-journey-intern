# ============================================
# File    : 17_Daily_Order_Report.py
# Purpose : Orders come as raw CSV lines. Some lines are empty,
#           some have missing fields, some names are empty,
#           and some numbers are wrong. We need a report we can trust.
# Concepts: Function with return, def, parameter, default parameter, for loop
# Issue   : #38
# Author  : Watacharapon
# Date    : 2026-11-09
# ============================================

MIN_QUANTITY = 1
# Main data (order_id, name, quantity, price)
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


# Function for claen name
def cleanName(name, default="UNKNOWN"):
    clean_name = name.strip().upper()
    if clean_name == "":
        return default
    else:
        return clean_name


# Function for check quantity munt not less then MIN_QUANTITY
def isValidQuantity(quantity, min_quantity=MIN_QUANTITY):
    if quantity >= min_quantity:
        return True
    else:
        return False


# Function for calulate amout of each order_id
def calculateTotal(quantity, price):
    total = quantity * price
    return total


# Function for sum of function calculateTotal
def addAll(total):
    sum_total = 0
    for i in total:
        sum_total += i
    return sum_total


# Part B Use function in loop
if orders != []:
    count_reject = 0
    count_valid = 0
    list_total = []
    printTitle("DAILY ORDER REPORT")
    for order_id, name, quantity, price in orders:
        reason = ""
        if isValidQuantity(quantity):
            total = calculateTotal(quantity, price)
            print(f"[{order_id}] {cleanName(name):<15} | {total:.2f} ")
            list_total.append(total)
            count_valid += 1
        else:
            print(f"[{order_id}] {cleanName(name):<15} | Quantity must be at least {MIN_QUANTITY} ")
            count_reject += 1
    print("-"*30)

    # Part C Summary
    label_valid_order = "Valid orders"
    label_rejected_order = "Rejected orders"
    label_grand_total = "Grand total"
    label_check_control = "Control check"
    grand_total = addAll(list_total)
    print(f"{label_valid_order:<25} : {count_valid}")
    print(f"{label_rejected_order:<25} : {count_reject}")
    print(f"{label_grand_total:<25} : {grand_total:.2f}")
    if count_valid + count_reject == len(orders):
        result1 = "PASS"
    else:
        result1 = "FAIL"
    print(f"{label_check_control:<25} : {result1}")
    print("-"*30)
else:
    print("No orders to check")
# Part D test default value and edge case
result = isValidQuantity(2, min_quantity=3)
print(f"[TEST] quantity 2, min 3 -> {result}")