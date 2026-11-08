# ============================================
# File    : 16_Daily_Order_Check.py
# Purpose : Clean customer names and check order amounts
#           with simple functions.
# Concepts: def, parameter, default parameter, for loop
# Issue   : #36
# Author  : Watacharapon
# Date    : 2026-11-08
# ============================================

# Test data: (order_id, raw_name, amount)
orders = [
    ("A001", "  somchai  ", 250.5),
    ("A002", "MALI", 50),
    ("A003", " john ", 100),
    ("A004", "   ", 300),
]
MIN_AMOUNT = 100

# Part A Create function
# Function Print a title with lines
def printTitle(title, symbol="="):
    print(symbol*30)
    print(title)
    print(symbol*30)


# Function Clean the name and print
def showCleanName(order_id, raw_name):
    clean_name = raw_name.strip().upper()
    if clean_name != "":
        print(f"[{order_id}] Clean name : {clean_name}")
    else:
        print(f"[{order_id}] Clean name : EMPTY NAME")


# Function Check amount
def checkAmount(order_id, amount, min_amount=MIN_AMOUNT):
    if amount >= min_amount:
        print(f"[{order_id}] Amount {amount:.2f} -> PASS")
    else:
        print(f"[{order_id}] Amount {amount:.2f} -> FAIL (minimum is {min_amount})")


# Function Print the summary
def printSummary(total, passed, failed):
    printTitle("SUMMARY", "-")
    print(f"Total orders : {total}")
    print(f"Passed       : {passed}")
    print(f"Failed       : {failed}")
    print("-"*30)


# Part B Call function
printTitle("DAILY ORDER CHECK", "=")
passed = 0
failed = 0
for order_id, raw_name, amount in orders:
    showCleanName(order_id, raw_name)
    checkAmount(order_id, amount)
    if amount >= MIN_AMOUNT:
        passed += 1
    else:
        failed += 1
printSummary(len(orders), passed, failed)
checkAmount("TEST", 150, min_amount=200)