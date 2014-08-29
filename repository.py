#!/usr/bin/python
ACTIVITY_NAME_COL = 3
TITLE_COL = 4
STAGED_COL = 9
COPIED_COL = 8
NOPTA_FILE = "/nas/energy/ideas/RDIS/NOPIMS_repository_remediation/NOPTA_20120101_20140728_OpenFile_Well_List.xlsx"
NOPTA_SHEET_NAME = "NOPTA-OF-Wells"
WELLS_ROOT = "/nas/pmd/repos/open/Wells/Regulated"


import os, re, xlrd

def run_me():
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
            if state_folder == "T": # catch the 'T' instance
                state_folder = "TAS"
            activity_name= activity_name_parse(row[ACTIVITY_NAME_COL].value)
            if os.path.join(WELLS_ROOT,state_folder):
                search_path = os.path.join(WELLS_ROOT,state_folder)
                find_dirs(search_path,activity_name)
            else:
                search_path = WELLS_ROOT
                print(search_path)
                print activity_name
        i += 1

def find_dirs(sp, an, lvl = 1):
    dirs=os.listdir(sp)
    directories = filter(lambda x: an in x, dirs)
    if directories.__len__ > 1:
        print directories
#
#  for filename in filenames:
#    print os.path.join(dirname, filename)

def activity_name_parse(string):
    string = re.sub("\([^)]+\)",'',string).strip() # Remove parentheses and strip trailing and leading spaces
    string =  re.sub("(ST([0-9])|L([0-9]))",'',string).strip() #Remove SH
    return string.replace(' ','_')

run_me()
    
