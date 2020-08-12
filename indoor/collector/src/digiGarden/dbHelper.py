import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="digigarden"
)

def addSolarData(solarData):
    mycursor = mydb.cursor()
    sql = "INSERT INTO solarControllerData (batteryVoltage, solarVoltage, chargingCurrent, loadCurrent) VALUES (%s, %s, %s, %s)"
    val = (1, 2, 3, 4)
    mycursor.execute(sql, solarData)
    mydb.commit()
