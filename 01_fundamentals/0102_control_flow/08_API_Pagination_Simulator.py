# ============================================
# File : 08_API_Pagination_Simulator.py
# Purpose:  Practice using While Loop basic
#           This task simulates that using a while loop 
#           that keeps running until no more data is left
#           by return results in “pages”.
# Author: Watacharapon
# ============================================

# Declaring variable constant
TOTAL_RECORDS = 47            
PAGE_SIZE = 10                  
SAFETY_TIMES = 100

# use counter loop 
page_counter = 0                # counts pages for the report
records_fetched = 0             # for store value to fetched
records_page_size = 0
safety_counter = 0              # counts loops to stop an infinite loop

# use display
separator = "="
title = "API Pagination Simulator"
title_display_1 = "Total records in system"
title_display_2 = "Page size"
title_summary = "Summary"
summary_display_1 = "Total pages fetched"
summary_display_2 = "Total records fetched"
summary_display_3 = "Status"

# Section display process of fetched
print(f"{separator*5} {title} {separator*5}")
print(f"{title_display_1} : {TOTAL_RECORDS}")
print(f"{title_display_2} : {PAGE_SIZE}")
print("")
print(f"{separator*50}")
# Process while loop
while records_fetched < TOTAL_RECORDS:
    # Safety counter: stop the loop if it runs too many times
    # so a bug cannot make the program run forever (infinite loop)
    safety_counter += 1
    if safety_counter > SAFETY_TIMES:
        print("Safety limit reached")
        break
    # section calculate fetch data
    page_counter += 1
    records_fetched += PAGE_SIZE
    # Check the last page and keep only the remaining data.
    if records_fetched > TOTAL_RECORDS:
        records_fetched += TOTAL_RECORDS-records_fetched
    # Check the records on each page and calculate the remaining records.
    if records_fetched%PAGE_SIZE == 0:
        records_page_size = PAGE_SIZE
    else:
        records_page_size = records_fetched%PAGE_SIZE
    # section display process fetched
    print(f"Fetching page {page_counter}... got {records_page_size} records (total so far: {records_fetched})")
print(f"{separator*50}")
# section summary
print(f"{separator*5} {title_summary} {separator*5}")
print(f"{summary_display_1:<25} : {page_counter}")
print(f"{summary_display_2:<25} : {records_fetched}")
if safety_counter <= SAFETY_TIMES:
    print(f"{summary_display_3:<25} : Complete")
else:
    print(f"{summary_display_3:<25} : Incomplete (Safety limit reached)")