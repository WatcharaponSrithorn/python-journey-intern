# ============================================
# File : 08_API_Pagination_Simulator.py
# Purpose:  Practice using While Loop basic
#           This task simulates that using a while loop 
#           that keeps running until no more data is left
#           by return results in “pages”.
# Author: Watacharapon
# ============================================

# Declaring variable constant
TOTAL_RECORDS = 1005              # สมมติว่าระบบมีข้อมูลทั้งหมด___แถว
PAGE_SIZE = 10                  # แต่ละหน้าดึงมาได้ 10 แถว
SAFETY_TIMES = 100

# use counter loop 
page_counter = 0
records_fetched = 0             # for store value to fetched
records_page_size = 0
safety_counter = 0

# use display
separator = "="
title = "API Pagination Simulator"
title_display_1 = "Total records in system"
title_display_2 = "Page size"
title_summary = "Summary"
summary_display_1 = "Total pages fetched"
summary_display_2 = "Total records fetched"

# Section display process of fetched
print(f"{separator*5} {title} {separator*5}")
print(f"{title_display_1} : {TOTAL_RECORDS}")
print(f"{title_display_2} : {PAGE_SIZE}")
print("")
print(f"{separator*50}")
# Process while loop
while records_fetched < TOTAL_RECORDS:
    # check safety counter
    safety_counter += 1
    if safety_counter > SAFETY_TIMES:
        print("Safety limit reached")
        break
    # section calculate fetch data
    page_counter += 1
    records_fetched += PAGE_SIZE
    # check Last page ให้เก็บค่าแค่ ส่วนที่เหลือ
    if records_fetched > TOTAL_RECORDS:
        records_fetched += TOTAL_RECORDS-records_fetched
    # check each page record how and calcual ส่วนที่เหลือ
    if records_fetched%PAGE_SIZE == 0:
        records_page_size = PAGE_SIZE
    else:
        records_page_size = records_fetched%PAGE_SIZE
    # section display preocee fetched
    print(f"Fetching page {page_counter}..got to {records_page_size} records (total so far: {records_fetched}) ")
print(f"{separator*50}")
# section summary
print(f"{separator*5} {title_summary} {separator*5}")
print(f"{summary_display_1} : {page_counter}")
print(f"{summary_display_2} : {records_fetched}")

