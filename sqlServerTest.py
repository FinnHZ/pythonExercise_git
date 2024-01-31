import pyodbc
import datetime as dt
import functools
import time

dbconn = None
dbuser = 'AUCOM-CO-NZ\\f.he'
dbpass = ''
dbhost = 'ENG-Testbay'
dbport = '1433'
dbname = 'TestPythonDB'  #'FpDb'



timesList = []

time0 = dt.datetime.now()   ####################################################### 0
timesList.append(time0)
time.sleep(1)

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=%s;PORT=%s;DATABASE=%s;UID=%s; PWD=%s; Trusted_Connection=yes;'%(dbhost, dbport, dbname, dbuser,dbpass))

time1 = dt.datetime.now()   ####################################################### 1
timesList.append(time1)
time.sleep(1)

cursor = cnxn.cursor()

time2 = dt.datetime.now()   ####################################################### 2
timesList.append(time2)
time.sleep(1)

# Execute a query
cursor.execute("SELECT * FROM dbo.Table_1")

time3 = dt.datetime.now()   ####################################################### 3
timesList.append(time3)
time.sleep(1)

# Fetch the results
results = cursor.fetchall()

time4 = dt.datetime.now()   ####################################################### 4
timesList.append(time4)
time.sleep(1)

# Iterate over the results and print each row
for row in results:
    print(row)

time5 = dt.datetime.now()   ####################################################### 5
timesList.append(time5)
time.sleep(1)


def dateMinus(listObj):
    i = 0
    while i < len(listObj)-1:
        x = listObj[i]
        y = listObj[i+1]
        s1 = str(timesList.index(y)) + "-" + str(timesList.index(x)) 
        s2 = str(y - x)[4:]
        s3 = s1 + ":" + s2
        print(s3)
        i += 1

dateMinus(timesList)


