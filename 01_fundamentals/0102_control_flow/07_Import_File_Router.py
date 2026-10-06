# ============================================
# File : 07_Import_File_Router.py 
# Purpose:  Practice using Match statement basic
#           Receive files from many sources with different extensions, 
#           and each type needs different processing.
# Author: Watacharapon
# ============================================

# Declaring variable
title_program = "Import File Router"
separator_1 = "="
result_process = ""     # for store value in match to split process
result_warning = ""
title_summary = "ROUTING RESULT"
display_1 = "File"
display_2 = "Extension"
display_3 = "Action"
display_4 = "Warning"

# Input Ask the user
print(f"{separator_1*5} {title_program} {separator_1*5}")
file_name = input("Enter file name : ")                     # Receive for split extension
file_size_mb = float(input("Enter file size (MB) : "))     # Receive for use verify condition special process 

# Process 
# Section split extension is list 
# add index [-1] case to have dot . more one
ext = file_name.split(".")[-1]
ext_lower = ext.lower()              # for duplicate code in case not  CSV | csv

# Section Match for split process
match ext_lower:
    case "csv" :           
        result_process = "Process as CSV: read rows and columns"
        if file_size_mb > 100:
            result_warning = "Warning: large file, consider chunked reading"
    case "json":
        result_process = "Process as JSON: parse as dictionary"
    case "xml"| "txt":
        result_process = "Process as plain text: needs manual parsing"
    case _:                                             # use protect against unknown file extension 
        result_process = "Unknown file type : cannot process"

# Section Readable Summary display
print("")
print(f"{separator_1*50}")
print(f"{title_sumary:^50}")
print(f"{separator_1*50}")
print(f"{display_1:<25} : {file_name}")
print(f"{display_2:<25} : {ext_lower}")
print(f"{display_3:<25} : {result_process}")
if result_warning != "":                      
    print(f"{display_4:<25} : {result_warning}")