#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:45:48 2019

@author: r.mishra
"""

import apiclient.discovery
import httplib2
import oauth2client
import re
import requests
##import shutil
import urllib.parse


SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
SPREADSHEET_ID = '1y4c0z12IWhhnE54eg4YTwH3teYTURQ5BbCT88eRVYNk'

store = oauth2client.file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
  flow = oauth2client.client.flow_from_clientsecrets('SheetAccess.json', SCOPES)
  creds = oauth2client.tools.run_flow(flow, store)


service = apiclient.discovery.build('sheets', 'v4', http=creds.authorize(httplib2.Http()))

result = service.spreadsheets().get(spreadsheetId = SPREADSHEET_ID).execute()
spreadsheetUrl = result['https://docs.google.com/spreadsheets/d/1y4c0z12IWhhnE54eg4YTwH3teYTURQ5BbCT88eRVYNk/edit#gid=0']
exportUrl = re.sub("\/edit$", '/export', spreadsheetUrl)
headers = {
  'Authorization': 'Bearer ' + creds.access_token,
}
for sheet in result['sheets']:
  params = {
    'format': 'csv',
    'gid': sheet['properties']['sheetId'],
  } 
  queryParams = urllib.parse.urlencode(params)
  url = exportUrl + '?' + queryParams
  response = requests.get(url, headers = headers)
  filePath = '/tmp/foo-%s.csv' % (+ params['gid'])
  with open(filePath, 'wb') as csvFile:
    csvFile.write(response.content)