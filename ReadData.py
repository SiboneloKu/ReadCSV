import pymysql
from datetime import datetime

csv_file=open(r"C:\\test\\google_stock_data.csv","r")
read_file=csv_file.read()

Data_list=[]
for line in read_file.split('\n'):
    Data_list.append(line.split(','))


#connect to the database
db=pymysql.connect("localhost","root","","google_stocks")
#preparing the cursor()
cursor=db.cursor()
Date=Data_list[0][0]; Open=Data_list[0][1]; High=Data_list[0][2]; Low=Data_list[0][3]; Close=Data_list[0][4]; Volume=Data_list[0][5]; Adj_Close=Data_list[0][6]
cursor.execute("DROP TABLE IF EXISTS GOOGLEDATA")
sql="""CREATE TABLE GOOGLEDATA (
        DATE nvarchar(225) NOT NULL,
        0pen FLOAT,
        High FLOAT,
        Low  FLOAT,
        Close FLOAT,
        Volume FLOAT,
        Ad_Close FLOAT )"""
cursor.execute(sql)
del Data_list[0]

rows=''

for k in range(len(Data_list)-1):
    rows+="('{}','{}','{}','{}','{}','{}','{}')".format(Data_list[k][0], Data_list[k][1], Data_list[k][2], Data_list[k][3], Data_list[k][4], Data_list[k][5], Data_list[k][6])
    if k !=len(Data_list)-2:
        rows+=','

queryInsert="INSERT INTO GOOGLEDATA VALUES"+ rows

try:
    #Run the SQL command
    cursor.execute(queryInsert)
    db.commit()
    print("Query executed")
except:
    db.rollback()
db.close()

