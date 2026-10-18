# ============================================
# File : 13_Customer_ID_Reconciliation.py
# Purpose:  Check if two systems have the same customers. Find who is missing.
#           with set, set operations, list, tuple, for loop
# Author: Watacharapon
# ============================================

# Variable sample data
crm_ids = [" cus-001", "CUS-002", "cus-003 ", "CUS-004", "cus-002", "", "CUS-006"]
billing_ids = ["CUS-002", "cus-003", "CUS-005", " cus-006 ", "CUS-006", "xyz-009", ""]
closed_ids = ("CUS-006", "CUS-099")

# Variable
valid_ids_crm = []                      # for store to clean and valid CRM
invalid_ids_crm = []                    # for store to invalid CRM
count_empty_values_crm = 0              # for store to count empty CRM
valid_ids_billing = []                  # for store to clean and valid billing
invalid_ids_billing = []                # for store to invalid billing
count_empty_values_billing = 0          # for store to count empty billing

# variable for display
separator = "="
hyphen = "-"
title_program = "Customer ID Reconciliation Report"
column_1 = "Source"
column_2 = "Rows"
column_3 = "Empty"
column_4 = "Invalid"
column_5 = "Duplicates"
column_6 = "Unique"
row_crm = "CRM"
row_billing = "Billing"
label_invalid_ids = "Invalid IDs"
label_closed_ids_excluded = "Closed IDs excluded"
label_all_customer = "All customers"
label_match_rate = "Match rate"
label_status = "Status"


# Casting for remove closed IDs from both systems.
set_closed_ids = set(closed_ids)

# System CRM
# Section cleaning data both system before validation
# Clean
for data in crm_ids:
    data = data.strip().upper()
    # validation then store valid and invalid
    if data == "":
        count_empty_values_crm += 1
    elif not data.startswith("CUS-"):
        invalid_ids_crm.append(data)
    else:
        valid_ids_crm.append(data)
set_of_valids_crm = set(valid_ids_crm)
# Section calculate count duplicate
count_duplicates_ids_crm = len(valid_ids_crm) - len(set_of_valids_crm)
# validation Closed IDs excluded
closed_ids_excluded_crm = set_closed_ids & set_of_valids_crm
# Section remove closed IDs
crm_ids_after_closed = set_of_valids_crm - set_closed_ids

# System Billing
# Section cleaning data both system before validation
# Clean
for data in billing_ids:
    data = data.strip().upper()
    # validation then store valid and invalid
    if data == "":
        count_empty_values_billing += 1
    elif not data.startswith("CUS-"):
        invalid_ids_billing.append(data)
    else:
        valid_ids_billing.append(data)
set_of_valids_billing = set(valid_ids_billing)
# Section calculate count duplicate
count_duplicates_ids_billing = len(valid_ids_billing) - len(set_of_valids_billing)
# validation Closed IDs excluded
closed_ids_excluded_billing = set_closed_ids & set_of_valids_billing
# Section remove closed IDs
billing_ids_after_closed = set_of_valids_billing - set_closed_ids

# Section display report summary
# Union Closed IDs excluded and sort for display
closed_ids_excluded = closed_ids_excluded_billing | closed_ids_excluded_crm
list_closed_ids_excluded = list(closed_ids_excluded)
list_closed_ids_excluded.sort()
# Compare the data using set operations.
# Store the 3 results as a list of tuples. Print them with one for loop.
list_in_both = list(billing_ids_after_closed & crm_ids_after_closed)
list_in_both.sort()
list_only_crm = list(crm_ids_after_closed - billing_ids_after_closed)
list_only_crm.sort()
list_only_billing = list(billing_ids_after_closed - crm_ids_after_closed)
list_only_billing.sort()

comparison_results = [
    ("In both systems", list_in_both),
    ("Only in CRM", list_only_crm),
    ("Only in Billing", list_only_billing)
]
all_customers = crm_ids_after_closed | billing_ids_after_closed
# Invalid IDs both system
invalid_ids_both = set(invalid_ids_billing) | set(invalid_ids_crm)
list_invalid_ids_both = list(invalid_ids_both)
list_invalid_ids_both.sort()
# Section check all customer before calculate Match rate protect value 0
if len(all_customers) != 0:
    # calculate Match rate
    match_rate = (len(list_in_both) / len(all_customers)) * 100
    if len(list_only_crm) == 0 and len(list_only_billing) == 0:
        status = "MATCHED"
    else:
        status = "MISMATCH"

# Section Display
print(f"\n{separator*5} {title_program} {separator*5}")
print(f"{hyphen*65}")
print(f"{column_1:<12}| {column_2:<8}| {column_3:<8}| {column_4:<8}| {column_5:<12}| {column_6:<8}")
print(f"{row_crm:<12}| {len(crm_ids):<8}| {count_empty_values_crm:<8}| {len(invalid_ids_crm):<8}| {count_duplicates_ids_crm:<12}| {len(set_of_valids_crm):<8}")
print(f"{row_billing:<12}| {len(billing_ids):<8}| {count_empty_values_billing:<8}| {len(invalid_ids_billing):<8}| {count_duplicates_ids_billing:<12}| {len(set_of_valids_billing):<8}")
print(f"{hyphen*65}")
print(f"{label_invalid_ids:<25} : {list_invalid_ids_both}")
print(f"{label_closed_ids_excluded:<25} : {list_closed_ids_excluded}")
print(f"{hyphen*65}")
if len(all_customers) != 0:
    for label_compare_name, list_ids in comparison_results:
        print(f"{label_compare_name:<25} : {len(list_ids)} -> {list_ids}")
    print(f"{label_all_customer:<25} : {len(all_customers)}")
    print(f"{label_match_rate:<25} : {match_rate:.1f}%")
    print(f"{label_status:<25} : {status}")
    print(f"{hyphen*65}\n")
else:
    print("No customer to compare")
    print(f"{hyphen*65}\n")