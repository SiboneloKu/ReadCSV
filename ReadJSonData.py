import pymysql
import json
import csv

# converting CSV File to JSon File
csvFile = "F:\Documents\Developer Work\Python\python_pract\StockMarket .csv"
jsonFile = "Google.json"

data = {}
with open(csvFile) as csvFilePath:
    csvReader = csv.DictReader(csvFilePath)
    for csvRow in csvReader:
        Date = csvRow["Date"]
        data[Date] = csvRow

with open(jsonFile, "w") as jsonFilePath:
    jsonFilePath.write(json.dumps(data, indent=4))

# Loading the converted file to mysql database
JSonFileFile_path = "F:\Documents\Developer Work\Python\python_pract\Google.json"
JData = open(JSonFileFile_path).read()
J_object = json.loads(JData)

# connecting to the database
con = pymysql.connect("localhost", "root", "", "google_stocks")
cursor = con.cursor()

# Looping onto the items and adding each row to the GOOGLEDATA Table
for Json_items in J_object:
    Date = str(J_object[Json_items]["Date"])
    Open = float(J_object[Json_items]["Open"])
    High = float(J_object[Json_items]["High"])
    Low = float(J_object[Json_items]["Low"])
    Close = float(J_object[Json_items]["Close"])
    Volume = float(J_object[Json_items]["Volume"])
    Ad_Close = float(J_object[Json_items]["Adj Close"])
    cursor.execute("INSERT INTO GOOGLEDATA (DATE, Open, High, Low, Close, Volume, Adj_Close) VALUE (%s, %s, %s, %s, %s, %s, %s)",(Date, Open, High, Low, Close, Volume, Ad_Close))

try:

    con.commit()
    print("Successful")
except:
    con.rollback()
    print("Unsuccessful")
con.close()










