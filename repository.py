#!/usr/bin/python
ACTIVITY_NAME_COL = 3
STAGED_COL = 9
COPIED_COL = 8
NOPTA_FILE = '/Users/michael/Public/nopims/NOPTA_20120101_20140728_OpenFile_Well_List.xlsx'
NOPTA_SHEET_NAME = "NOPTA-OF-Wells"
WELLS_ROOT = '/nas/pmd/repos/open/Wells/Regulated'


import os
import openpyxl as px

workbook = px.load_workbook(NOPTA_FILE,use_iterators = True)

sheet = workbook.get_sheet_by_name(name = NOPTA_SHEET_NAME)

for row in sheet.iter_rows():
    staged = row[STAGED_COL].value
    copied = row[COPIED_COL].value
    if not staged and not copied:
        activity_name = row[ACTIVITY_NAME_COL].value
        directory_string = activity_name.replace(' ','_')
        for root, dirs, files in os.walk(WELLS_ROOT):
            print dirs
    

#
#  for filename in filenames:
#    print os.path.join(dirname, filename)
