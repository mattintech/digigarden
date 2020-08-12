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
    sql = """INSERT INTO piData (hostname, wlan_ipaddress, cpu_usage, total_memory, free_memory, free_space, 
    pi_temperature, system_boot_time, system_uptime) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    insertData(sql, piData)