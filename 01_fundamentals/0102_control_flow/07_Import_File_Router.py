# ============================================
# File : 07_Import_File_Router.py 
# Purpose:  Practice using Match statement basic
#           Receive files from many sources with different extensions, 
#           and each type needs different processing.
# Author: Watacharapon
# ============================================

# Declaring varible
title_program = "Import File Router"
separator_1 = "="
result_process = ""     # for store value in match to split process
result_warning = ""
title_sumary = "ROUTING RESULT"
display_1 = "File"
display_2 = "Extension"
display_3 = "Action"
display_4 = "Warning"

# Input Ask the user
print(f"{separator_1*5} {title_program} {separator_1*5}")
file_name = input("Enter file name : ")             # Receive for split extension
file_size_mb = float(input("Enter file size (MB) : "))     # Receive for use verify condition special process 

# Process 
# Section split extension 
root, ext = file_name.split(".")        # Use unpacking because .split is List for file extension perform in match

# Section Match for split process
match ext:
    case "csv" | "CSV" if file_size_mb > 100:           # use verify condition continue of size
        result_process = "Process as CSV: read rows and columns"
        result_warning = "Warning: large file, consider chunked reading"
    case "csv" | "CSV" :
        result_process = "Process as CSV: read rows and columns"
    case "json" | "JSON":
        result_process = "Process as JSON: parse as dictionary"
    case "xml" | "XML" | "txt" | "TXT":
        result_process = "Process as plain text: needs manual parsing"
    case _:                                             # use protet file extention unknow 
        result_process = "Unknown file type : cannot process"

# Section Readable Summary display
print("")
print(f"{separator_1*50}")
print(f"{title_sumary:^50}")
print(f"{separator_1*50}")
print(f"{display_1:<25} : {file_name}")
print(f"{display_2:<25} : {ext}")
print(f"{display_3:<25} : {result_process}")
if ext == "CSV" or "csv":
    print(f"{display_4:<25} : {result_warning}")