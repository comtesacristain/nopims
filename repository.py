#!/usr/bin/python
ACTIVITY_NAME_COL = 3
TITLE_COL = 4
STAGED_COL = 9
COPIED_COL = 8
NOPTA_FILE = "/nas/energy/ideas/RDIS/NOPIMS repository documents remediation/NOPTA_20120101_20140728_OpenFile_Well_List.xlsx"
NOPTA_SHEET_NAME = "NOPTA-OF-Wells"
WELLS_ROOT = "/nas/pmd/repos/open/Wells/Regulated"


import os, re, xlrd

workbook = xlrd.open_workbook(NOPTA_FILE)

sheet = workbook.sheet_by_name(NOPTA_SHEET_NAME)

num_rows = sheet.nrows
i = 1

while i < num_rows:
    
    row = sheet.row(i)
    staged = row[STAGED_COL].value
    copied = row[COPIED_COL].value
    if not staged and not copied:
        state_folder = row[TITLE_COL].value.split('/')[0].split('-')[0]
        state_folder = re.sub("[0-9]",'',state_folder)
        activity_name = row[ACTIVITY_NAME_COL].value
        print state_folder
        #print activity_name
    i += 1
        #directory_string = activity_name.replace(' ','_')
        #for root, dirs, files in os.walk(WELLS_ROOT):
            #print dirs
    

#
#  for filename in filenames:
#    print os.path.join(dirname, filename)
