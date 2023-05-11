# =============PREDEFINED FUNCTIONS=================

# 01. FUNCTION TO READ GIVEN CSV TO LIST
# -----------------------------------------
def read_csv_to_list(filepath):
    import numpy as np

    list = []
    with open(filepath) as openfile:
        for line in openfile.readlines():
            if "#" not in line:
                list.append([float(value) for value in line.replace('\n', '').split(',')])
    return list




# 02. FUNCTION TO READ OPTIMAL PATH LIST TO CSV
# -----------------------------------------------
def read_list_to_csv(filename, list):
    import csv

    with open(filename, "w", newline='') as writefile:
        csv.writer(writefile).writerow(list)

