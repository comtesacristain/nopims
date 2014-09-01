#!/usr/bin/python
ACTIVITY_NAME_COL = 3
TITLE_COL = 4
STAGED_COL = 9
COPIED_COL = 8
NOPTA_FILE = "/nas/energy/ideas/RDIS/NOPIMS_repository_remediation/NOPTA_20120101_20140728_OpenFile_Well_List.xlsx"
NOPTA_SHEET_NAME = "NOPTA-OF-Wells"
WELLS_ROOT = "/nas/pmd/repos/open/Wells/Regulated"


associated_wells = []



import os, re, xlrd

def run_me():
    workbook = xlrd.open_workbook(NOPTA_FILE)
    sheet = workbook.sheet_by_name(NOPTA_SHEET_NAME)
    num_rows = sheet.nrows
    i = 1
    while i < num_rows:    
        row = sheet.row(i)
        title = row[TITLE_COL].value
        activity_name = row[ACTIVITY_NAME_COL].value
        staged = row[STAGED_COL].value
        copied = row[COPIED_COL].value
        if not staged and not copied:
            state_folder = title.split('/')[0].split('-')[0]
            state_folder = re.sub("[0-9]",'',state_folder)
            activity_key= activity_key_parse(activity_name)
            if os.path.isdir(os.path.join(WELLS_ROOT,state_folder)):
                search_path = os.path.join(WELLS_ROOT,state_folder)
                find_paths(search_path,activity_key)
            else:
                search_path = WELLS_ROOT
                paths=find_paths(search_path,activity_key,2)
                associate_wells_and_paths(title,activity_name,paths)
                print title
                print activity_name
                print paths
        i += 1

def associate_wells_and_paths(t,an,p):

    global associated_wells
    associated_wells[:]=[well for well in associated_wells if well.get("title") == t]
    print well
    associated_wells.append(well)
    

def find_paths(sp, ak, lvl = 1):
    directories = []
    dirs=os.listdir(sp)
    if lvl > 1:
        for x in dirs:
            directories += find_paths(os.path.join(sp,x),ak, lvl-1)
    directories += filter(lambda x: ak in x, dirs)
    return directories


def activity_key_parse(an):
    key = re.sub("\([^)]+\)",'',an).strip() # Remove parentheses and strip trailing and leading spaces
    key =  re.sub("(ST([0-9])|L([0-9]))",'',key).strip() #Remove SH
    return key.replace(' ','_')



run_me()
    
