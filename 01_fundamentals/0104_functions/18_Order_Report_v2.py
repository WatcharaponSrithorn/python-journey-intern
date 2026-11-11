# ============================================
# File    : 18_Order_Report_v2.py
# Purpose : Now we have small functions from #17.
#           Let’s combine them into bigger functions.
#           An order can also keep extra information, like channel or coupon,
#           without changing the function each time.
# Concepts: **kwargs, Function with return, *args,  def, parameter, default parameter, for loop
# Issue   : #40
# Author  : Watacharapon
# Date    : 2026-11-11
# ============================================

MIN_QUANTITY = 1
# Main data (order_id, raw_name, quantity, unit_price, chanal)
orders = [
    ("ORD-001", "  somchai  ", 2, 50.00, "WEB"),
    ("ORD-002", "MALI", 1, 120.50, "APP"),
    ("ORD-003", "   ", 3, 31.50, "WEB"),
    ("ORD-004", "john", 0, 45.00, "APP"),
    ("ORD-005", "  lisa", 4, 25.00, "STORE"),
]

# Part A Copy Function Form #17
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


# Part B Create Function buildOrder (use **kwargs and call function other)
def buildOrder(order_id, raw_name, quantity, unit_price, **extra):
    # create dictionary for store value 3 basic by call function
    order_new ={
        "order_id" : order_id,
        "name" : cleanName(raw_name),
        "total" : calculateTotal(quantity,unit_price)
    }
    # **kwargs add key/value in dictionary
    for key, value in extra.items():
        order_new[key] = value
    return order_new


# Part C (*args + call function + return multiple value)
def summarizeTotals (*total):
    grand_total = addAll(*total)
    count = 0
    count += len(total)
    if count != 0:
        average = grand_total / count
    else:
        average = 0
    return count, grand_total, average


# Part D printInfo (**kwargs for print)
def printInfo(title, symbol="-", **info):
    print(symbol*30)
    print(title)
    print(symbol*30)
    for key, value in info.items():
        label = key.replace("_", " ")
        print(f"{label:<16} : {value}")
    print(symbol*30)


# Part E: Use loop in DAILY ORDER REPORT and call function
if len(orders) != 0:
    count_reject = 0
    count_valid = 0
    list_total = []
    printTitle("DAILY ORDER REPORT")
    for order_id, raw_name, quantity, unit_price, channel in orders:
        if isValidQuantity(quantity):
            order = buildOrder(order_id, raw_name, quantity, unit_price, channel=channel)
            print(f"[{order.get('order_id')}] {order.get('name')} | {order.get('channel')} | {order.get('total'):.2f}")
            list_total.append(order.get('total'))
            count_valid += 1
        else:
            print(f"[{order_id}] REJECTED | Quantity must be at least {MIN_QUANTITY}")
            count_reject += 1
    count, grand_total, average = summarizeTotals(*list_total)
    text_grand_total = f"{grand_total:.2f}"
    text_average = f"{average:.2f}"
    if count_valid + count_reject == len(orders):
        control_result = "PASS"
    else:
        control_result = "FAIL"
    printInfo("Summary", valid_orders=count_valid, rejected_orders=count_reject, grand_total=text_grand_total, average=text_average, control_check=control_result)
else:
    print("No orders to check")

# Part F: Edge case and test end of file
print(f"[TEST-1] {"keys without extra : 3" if len(buildOrder("TEST-1", "  bob ", 2, 10.0)) <= 3 else buildOrder("TEST-1", "  bob ", 2, 10.0)}")
print(f"[TEST-2] {"keys without extra : 3" if len(buildOrder("TEST-2", "amy", 1, 5.0, coupon="NEW10", channel="APP")) <= 3 else buildOrder("TEST-2", "amy", 1, 5.0, coupon="NEW10", channel="APP")}")
