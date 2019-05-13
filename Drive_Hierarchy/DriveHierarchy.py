#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:42:23 2019

@author: r.mishra
"""
from __future__ import print_function
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import json

##Establish connection to Google Drive. Need to allow access once. 
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

CREDENTIAL_DIR = './credentials'
CREDENTIAL_FILENAME = 'credentials.json'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Drive File'
SCOPES = 'https://www.googleapis.com/auth/drive'

print("Accessing Google Drive(please click allow to desired drive)")

##Access and store drive credentails.

def get_credentials():
    credential_dir = CREDENTIAL_DIR
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, CREDENTIAL_FILENAME)

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

##Access Folders and files from Google Drive. Read Folders,files and it's detail and create a hierarchy tree.

def ListFolder(parent):
 filelist=[]
 file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % parent}).GetList()
 for f in file_list:
   if f['mimeType']=='application/vnd.google-apps.folder': # if folder
       filelist.append({"mimeType":f['mimeType'],"version":f['version'],"id":f['id'],"title":f['title'],"modifiedDate":f['modifiedDate'],"createdDate":f['createdDate'],"lastModifyingUserName":f['lastModifyingUserName'],"list":ListFolder(f['id'])})
   else:
       filelist.append({"mimeType":f['mimeType'],"version":f['version'],"title":f['title'],"modifiedDate":f['modifiedDate'],"createdDate":f['createdDate'],"lastModifyingUserName":f['lastModifyingUserName']})
 return filelist

res = ListFolder('root')

print("Data is ready Please write res and enter on console to get data")
    

##print(res)
    
    
    