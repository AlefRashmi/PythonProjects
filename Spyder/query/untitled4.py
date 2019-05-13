import psycopg2
import datetime
import numpy
from datetime import date, timedelta

## import pandas as pd

##import cur

con=psycopg2.connect("dbname=alefdatalake host=bg-nat.alefed.com port=5439 user=alef_bd_ireland password=A3fgh789po")


##cur = con.cursor()

##cur.execute(statement)

cur = con.cursor()
now = datetime.datetime.now()
##today = datetime.datetime.today().strftime('%Y-%m-%d')
today = str(datetime.date.today()).replace('-','')

##cur.execute('SELECT * FROM notes')
print(today)
date1 = str(date(2019, 1, 20)).replace('-','')
date2 = (date1,)
N=7
while date1 < today:
   #sql="SELECT a.subject_gen_subject, cast(avg(a.lesson_no) as FLOAT), max(a.week_num) as week from (SELECT lo.fle_student_dw_id,lo.subject_gen_subject, cast(count(distinct lo.fle_lo_dw_id) as FLOAT) as lesson_no, date_part('week',max(lo.full_date))-2 as week_num from alefdw.learning_experience_view lo where lo.full_date >= 20190113 and lo.full_date < ? and lo.fle_lesson_type='SA' and lo.fle_tenant_dw_id=2 and lo.fle_attempt=1 and lo.school_name!='Alef School' group by lo.fle_student_dw_id,lo.subject_gen_subject) a group by a.subject_gen_subject"
   print(date1)
   cur.execute("SELECT a.subject_gen_subject, cast(avg(a.lesson_no) as FLOAT),\
            max(a.week_num) as week from (SELECT lo.fle_student_dw_id,lo.subject_gen_subject,\
            cast(count(distinct lo.fle_lo_dw_id) as FLOAT) as lesson_no, \
            date_part('week',max(lo.full_date))-2 as week_num from alefdw.learning_experience_view \
            lo where lo.date_id >= 20190113 and lo.date_id < %s and lo.fle_lesson_type='SA' \
            and lo.fle_tenant_dw_id=2 and lo.fle_attempt=1 and lo.school_name!='Alef School' \
            group by lo.fle_student_dw_id,lo.subject_gen_subject) a group by a.subject_gen_subject",(date2))
   
   result = cur.fetchall()

   print(result)
   for r in result:
        print(r)
    ## print(date1)
    
   date1 = date1 + timedelta(days=N)
 
    
   
   
      
  
 



##cur.execute(sql)

con.commit()
