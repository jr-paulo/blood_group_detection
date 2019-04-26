
import pandas as pd 
import datetime
import main
import pymysql

PATH = '/Users/albinpaulose/blood_group_detection/app/static/img/faces/'

def detect_group(name,gender,dob,filename):
   print ("FILENAME", filename)
   
   blood_group = main.detectBlood(PATH+filename+".jpg")
   insert_log(name,gender,dob,blood_group)
   return blood_group

def insert_log(name,gender,dob,blood_group):
  db = pymysql.connect("localhost","root","","blood_detection" )
  cursor = db.cursor()
  now = datetime.datetime.now()
  sql = "insert into history(name,dob,gender,blood_group) values ('"+ name +"','"+ dob +"','"+ gender +"','"+ blood_group +"')"
  try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
  except:
   # Rollback in case there is any error
   print("inside exceptt")
   db.rollback()
def get_all_logs():
    db = pymysql.connect("localhost","root","","blood_detection" )
    cursor = db.cursor()
    sql = "select * from history order by id desc"   
    cursor = db.cursor()
    try:
      # Execute the SQL command
      cursor.execute(sql)
      # Fetch all the rows in a list of lists.
      results = cursor.fetchall()
      logs = []
      
     
      for row in results:
        logs.append([row[0],row[1],row[2],row[3],row[4],row[5]])
        
        # Now print fetched result
      return logs
    except:
        print ("Error: unable to fetch data")

