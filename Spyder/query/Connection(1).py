#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:38:30 2019

@author: r.mishra
"""



import psycopg2
import datetime

 ## import pandas as pd

##import cur

con=psycopg2.connect("dbname=alefdatalake host=bg-nat.alefed.com port=5439 user=alef_bd_ireland password=A3fgh789po")


##cur = con.cursor()

##cur.execute(statement)

cur = con.cursor()
##def func1(date1,date2):
##cur.execute('SELECT * FROM notes')
    today = datetime.datetime.today().strftime('%Y-%m-%d'):
    
    date1 = '2019-01-13' 
    
    while date1 <= today:

sql = "SELECT a.subject_gen_subject, cast(avg(a.lesson_no) as FLOAT), max(a.week_num) as week from (SELECT lo.fle_student_dw_id,lo.subject_gen_subject, cast(count(distinct lo.fle_lo_dw_id) as FLOAT) as lesson_no, date_part('week',max(lo.full_date))-2 as week_num from alefdw.learning_experience_view lo where lo.full_date >= 20190113 and lo.full_date < '"+date2+"' and lo.fle_lesson_type='SA' and lo.fle_tenant_dw_id=2 and lo.fle_attempt=1 and lo.school_name!='Alef School' group by lo.fle_student_dw_id,lo.subject_gen_subject) a group by a.subject_gen_subject"

cur.execute(sql)

    date1+ = 7
    result = cur.fetchall() 
for r in result:
    print(r)

##cur.execute(sql)

con.commit()
