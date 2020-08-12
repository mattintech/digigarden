import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="digigarden"
)

def insertData(sqlQuery, values):
    mycursor = mydb.cursor()
    mycursor.execute(sqlQuery, values)
    mydb.commit()
    mycursor.close()

def addSolarData(solarData):
    sql = "INSERT INTO solarControllerData (batteryVoltage, solarVoltage, chargingCurrent, loadCurrent) VALUES (%s, %s, %s, %s)"
    insertData(sql, solarData)    

def piStatistics(piData):
    sql = "INSERT INTO piData (hostname, wlan_ipaddress, free_space) VALUES (%s, %s, %s)"
    insertData(sql, piData)