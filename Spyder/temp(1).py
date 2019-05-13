# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""






import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('SheetAccess.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open("Copy of pacing calender")




