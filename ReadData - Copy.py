import csv
import pymysql
from datetime import datetime

csv_file=open(r"C:\\test\\google_stock_data.csv","r")
read_file=csv_file.read()

Data_list=[]
for line in read_file.split('\n'):
    Data_list.append(line.split(','))
    print(str(line))

#connect to the database
db=pymysql.connect("localhost","root","","google_stocks")
#preparing the cursor()
cursor=db.cursor()
#Drop table if it exist
cursor.execute("DROP TABLE IF EXISTS GOOGLE_DATA")

#creat the column name of the Data_list

Date=Data_list[0][0];Open=Data_list[0][1];High=Data_list[0][2];Low=Data_list[0][3];Close=Data_list[0][4];Volume=Data_list[0][5];Adj_Close=Data_list[0][6]

#Creating GOOGLE_DATA table
queryCreateGOOGLE_DATAtable="""CREATE TABLE DATA(
                                {} varchar(255) not null,
                                {} varchar(255),
                                {} varchar(255),
                                {} varchar(255),
                                {} varchar(255),
                                {} varchar(255),
                                {} varchar(255)
                                )""".format(Date,Open,High,Low,Close,Volume,Adj_Close)
cursor.execute(queryCreateGOOGLE_DATAtable)
#Removing the First raw in my Data_list[]
del Data_list[0]

rows=''
for k in range(len(Data_list)-1):
    rows+="('{}','{}','{}','{}','{}','{}','{}')".format(Data_list[i][0],Data_list[i][1],Data_list[i][2],Data_list[i][3],Data_list[i][4],Data_list[i][5],Data_list[i][6])
    if k !=len(Data_list)-2:
        rows+=','

#print(rows)
queryInsert="INSERT INTO GOOGLE_DATA VALUES"+rows
try:
    #Run the SQL command
    cursor.execute(queryInsert)
    db.commit()
    print("Query executed")
except:
    db.rollback()

db.close()









