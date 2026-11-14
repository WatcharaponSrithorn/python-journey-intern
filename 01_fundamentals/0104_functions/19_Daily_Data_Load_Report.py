# ============================================
# File    : 19_Daily_Data_Load_Report.py
# Purpose : Every morning, our load job reads data from many sources.
#           The team wants a short report: rows read, rows rejected,
#           and quality for each source.
# Concepts: **kwargs, Function with return, *args, def, parameter, default parameter, for loop
# Issue   : #42
# Author  : Watacharapon
# Date    : 2026-11-14
# ============================================

# variable constant
MIN_SUCCESS_RATE = 95.0

# main data = (name, rows_all, row_reject, soruce)
sources = [
    ("  orders_csv ", 1000, 20, "sales"),
    ("CUSTOMERS_API", 500, 40, "crm"),
    ("   ", 200, 0, "sales"),
    ("returns_db", 0, 0, "ops"),
    ("  payments_csv", 800, 8, "finance"),
]

# Part A : Copy 3 function Form #18
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

# Part D printInfo (**kwargs for print)
def printInfo(title, symbol="-", **info):
    print(symbol*30)
    print(title)
    print(symbol*30)
    for key, value in info.items():
        label = key.replace("_", " ")
        print(f"{label:<16} : {value}")
    print(symbol*30)

# Part B : Calculate Success Rate
def calculateSuccessRate(rows_read, rows_rejected):
    if rows_read != 0:
        rows_good = rows_read - rows_rejected
        percent =  (rows_good * 100) / rows_read
        return percent
    else:
        return 0

# Part C Quality Gate
def isGoodQuality(success_rate, min_rate=MIN_SUCCESS_RATE):
    if success_rate >= min_rate:
        return True
    else:
        return False

# Part D Sum Rows (*args)
def sumRows(*args):
    sum_rows = 0
    for number in args:
        sum_rows += number
    return sum_rows

# Part E Build Run Record (**kwargs + call function other)
def buildRunRecord(raw_name, rows_read, row_reject, **extra):
    dict_record ={
        "source" : cleanName(raw_name),
        "rows_read" : rows_read,
        "row_reject" : row_reject,
        "success_rate" : calculateSuccessRate(rows_read, row_reject)
    }
    for key, value in extra.items():
        dict_record.update({key : value})
    return dict_record

# Part F Run Stats (return multiply values)
def getRunStats(*row_counts):
    count = len(row_counts)
    total = sumRows(*row_counts)
    if count != 0:
        average = total/count
    else:
        average = 0
    return count, total, average

# Part G : Mian report (Main loop)
count_passed = 0
count_failed = 0
count_skipped = 0

if len(sources) == 0:
    print("No sources to check")
else:
    printTitle("DAILY DATA LOAD REPORT")
    for raw_name, rows_read, rows_rejected, team in sources:
        if rows_read > 0:
            dict_record = buildRunRecord(raw_name, rows_read, rows_rejected, team=team)
            if isGoodQuality(dict_record.get('success_rate'), min_rate=MIN_SUCCESS_RATE):
                print(f"[PASS] {dict_record.get('source')} | {dict_record.get('team')} | read {dict_record.get('rows_read')} | rejected {dict_record.get('row_reject')} | success {dict_record.get('success_rate'):.2f}%")
                count_passed += 1
            else:
                print(f"[FAIL] {dict_record.get('source')} | {dict_record.get('team')} | read {dict_record.get('rows_read')} | rejected {dict_record.get('row_reject')} | success {dict_record.get('success_rate'):.2f}%")
                count_failed += 1
        else:
            print(f"[SKIP] {dict_record.get('source')} | no rows to load")
            count_skipped += 1
