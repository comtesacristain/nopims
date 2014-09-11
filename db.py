import db_settings
import sqlite3
#import master_record
import os, re, xlrd, xlwt, shutil

#NOPTA_FILE = "/nas/energy/ideas/RDIS/NOPIMS_repository_remediation/NOPTA_20120101_20140728_OpenFile_Well_List.xlsx"

NOPTA_FILE = "/Users/michael/Public/nopims/NOPTA_20120101_20140728_OpenFile_Well_List.xlsx"
NOPTA_SHEET_NAME = "NOPTA-OF-Wells"


def read_sheet():
    workbook = xlrd.open_workbook(NOPTA_FILE)
    sheet = workbook.sheet_by_name(NOPTA_SHEET_NAME)
    create_table("master")
    num_rows = sheet.nrows
    i = 1
    while i < num_rows:    
        row = sheet.row(i)
        print row
        i+=1
    
def write_sheet():
    return 0   

def get_curs():
    conn=sqlite3.connect('nopta.db')
    return conn.cursor()
    
def create_table(name):
    curs = get_curs()
    conn = curs.connection
    curs.execute(str.format("SELECT name FROM sqlite_master WHERE type='table' AND name='{0}';",name))
    if not curs.fetchone():
        curs.execute(str.format("CREATE TABLE {0} (date text, trans text, symbol text, qty real, price real);",name))
        conn.commit()
    conn.close()
read_sheet()