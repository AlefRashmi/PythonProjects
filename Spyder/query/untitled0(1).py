#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 12:06:35 2019

@author: r.mishra
"""

import psycopg2
import datetime
from datetime import timedelta


 ## import pandas as pd

##import cur

con=psycopg2.connect("dbname=alefdatalake host=bg-nat.alefed.com port=5439 user=alef_bd_ireland password=A3fgh789po")


##cur = con.cursor()

##cur.execute(statement)

cur = con.cursor()
now = datetime.datetime.now()
today = datetime.datetime.today().strftime('%Y-%m-%d')
x = datetime.date.today()
##cur.execute('SELECT * FROM notes')

sql = """SELECT a.subject_gen_subject, cast(avg(a.lesson_no) as FLOAT), max(a.week_num) as week from
(SELECT lo.fle_student_dw_id,lo.subject_gen_subject, cast(count(distinct lo.fle_lo_dw_id) as FLOAT) as lesson_no,
   date_part('week',max(lo.full_date))-2 as week_num
from alefdw.learning_experience_view lo
where lo.date_id >= 20190113 and date_id < 20190120
and lo.fle_lesson_type='SA'
and lo.fle_tenant_dw_id=2
and lo.fle_attempt=1
and lo.school_name!='Alef School'
group by lo.fle_student_dw_id,lo.subject_gen_subject) a
group by a.subject_gen_subject"""

cur.execute(sql)

result = cur.fetchall() 
for r in result:
    print(r)
print(now)
print(today)
print(x)
print(date(timedelta(N)))



##cur.execute(sql)

con.commit()
