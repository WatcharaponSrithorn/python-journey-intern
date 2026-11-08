# ============================================
# File : 16_Daily_Order_Check.py
# Purpose:  Orders come as a list of tuples.
#           Some names have extra spaces, some names
#           are empty, and some amounts are too low.
#           with create Function def, Parameter, Default value
# Author: Watacharapon
# ============================================

# Test data: (order_id, raw_name, amount)
orders = [
    ("A001", "  somchai  ", 250.5),
    ("A002", "MALI", 50),
    ("A003", " john ", 100),
    ("A004", "   ", 300),
]

count_pass = 0
count_fail = 0
count_order_id = 0

# Part A Copy from original
copy_orders = orders.copy()

# Part B Create function
# Function Print a title with lines
def printLitle(title,symbol = "="):
    # Declaring variable
    print(symbol*50)
    print(f"{title:^50}")
    print(symbol*50)

# Function Clean the name and print
def showCleanName(order_id, raw_name):
    if raw_name.strip() != "":
        print(f"[{order_id}] Clean name : {raw_name.strip().upper()}")
    else:
        print(f"[{order_id}] Clean name : EMPTY NAME")

# Function Check amount
def checkAmount(order_id, amount, min_amount = 100):
    global count_order_id
    global count_pass
    global count_fail
    count_order_id += 1
    if amount >= min_amount:
        count_pass += 1
        print(f"[{order_id}] Amount {amount} -> PASS ")
    else:
        count_fail += 1
        print(f"[{order_id}] Amount {amount} -> FAIL (minimum is {min_amount}) ")
    print(count_order_id)
# Function Print the summary
def printSummary(total, passed, failed):
    printLitle("SUMMARY", "-")
    print(f"Total orders : {total}")
    print(f"Passed       : {passed}")
    print(f"Failed       : {failed}")
    print("-"*50)

# Part C Cell function
printLitle("DAILY ORDER CHECK", "=")
for item in copy_orders:
    showCleanName(item[0],item[1])
    checkAmount(item[0], item[2])
printSummary(count_order_id,count_pass,count_fail)