#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:20:58 2019

@author: r.mishra
"""

import json
import gspread
from oauth2client.service_account  import ServiceAccountCredentials

json_key = json.load(open('SheetAccess.json')) # json credentials you downloaded earlier
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

file = gspread.authorize(credentials) # authenticate with Google
sheet = file.open("Copy of pacing calender").Math # open sheet





##pip install  google-api-python-client google-auth-httplib2 google-auth-oauthlib

