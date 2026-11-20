# ============================================
# File    : 19_Daily_Data_Load_Report.py
# Purpose : Print a daily data load report. Check data quality of each source
#           with return functions, *args, and **kwargs.
# Concepts: **kwargs, Function with return, *args, def, parameter, default parameter, for loop,
#           combining functions, return many values
# Issue   : #42
# Author  : Watacharapon
# Date    : 2026-11-14
# ============================================

# variable constant
MIN_SUCCESS_RATE = 95.0

# main data = (raw_name, rows_read, rows_rejected, team)
sources = [
    ("  orders_csv ", 1000, 20, "sales"),
    ("CUSTOMERS_API", 500, 40, "crm"),
    ("   ", 200, 0, "sales"),
    ("returns_db", 0, 0, "ops"),
    ("  payments_csv", 800, 8, "finance"),
]

# Part A : Copy 3 function From #18
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


# function for printInfo (**kwargs for print)
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
        percent = (rows_good * 100) / rows_read
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
def sumRows(*row_counts):
    sum_rows = 0
    for number in row_counts:
        sum_rows += number
    return sum_rows


# Part E Build Run Record (**kwargs + call function other)
def buildRunRecord(raw_name, rows_read, rows_rejected, **extra):
    dict_record = {
        "source": cleanName(raw_name),
        "rows_read": rows_read,
        "rows_rejected": rows_rejected,
        "success_rate": calculateSuccessRate(rows_read, rows_rejected)
    }
    for key, value in extra.items():
        dict_record[key] = value
    return dict_record


# Part F Run Stats (return multiply values)
def getRunStats(*row_counts):
    count = len(row_counts)
    total = sumRows(*row_counts)
    if count != 0:
        average = total / count
    else:
        average = 0
    return count, total, average


# Part G : Main report (Main loop)
count_passed = 0
count_failed = 0
count_skipped = 0
list_rows_read = []
list_rows_rejected = []

if len(sources) == 0:
    print("No sources to check")
else:
    printTitle("DAILY DATA LOAD REPORT")
    for raw_name, rows_read, rows_rejected, team in sources:
        if rows_read > 0:
            dict_record = buildRunRecord(raw_name, rows_read, rows_rejected, team=team)
            if isGoodQuality(dict_record['success_rate']):
                status = "PASS"
                count_passed += 1
            else:
                status = "FAIL"
                count_failed += 1
            print(f"[{status}] {dict_record['source']} | {dict_record['team']} | read {dict_record['rows_read']} | rejected {dict_record['rows_rejected']} | success {dict_record['success_rate']:.2f}%")
            list_rows_rejected.append(dict_record['rows_rejected'])
            list_rows_read.append(dict_record['rows_read'])
        else:
            clean_name = cleanName(raw_name)
            print(f"[SKIP] {clean_name} | no rows to load")
            count_skipped += 1
    count, total, average = getRunStats(*list_rows_read)
    sum_rows_reject = sumRows(*list_rows_rejected)
    overall_success = calculateSuccessRate(total, sum_rows_reject)
    text_overall_success = f"{overall_success:.2f}%"
    if (len(sources) == count+count_skipped) and (count_passed+count_failed) == count:
        result_control_check = "PASS"
    else:
        result_control_check = "FAIL"
    printInfo("SUMMARY", sources_loaded=count,
              sources_skipped=count_skipped,
              quality_passed=count_passed,
              quality_failed=count_failed,
              total_rows_read=total,
              total_rejected=sum_rows_reject,
              overall_success=text_overall_success,
              control_check=result_control_check)


# Part H : Edge case and Test end file
test_1 = buildRunRecord("  demo ", 100, 10)
print(f"[TEST] keys without extra : {len(test_1)}")
test_2 = buildRunRecord("demo", 100, 10, team="ops", env="PROD")
print(f"[TEST] {test_2}")
test_3 = getRunStats()
print(f"[TEST] stats with no sources : {test_3}")
test_4 = isGoodQuality(90.0, min_rate=85.0)
print(f"[TEST] quality 90.0 with min 85.0 : {test_4}")