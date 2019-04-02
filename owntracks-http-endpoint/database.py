import os, sys, sqlite3

class Database():
    def addPosition(payload):
        create_database()
        connection = sqlite3.connect("./tempdata.db")

    def create_database():
    if not os.path.exists("./database.db"):
        connection = sqlite3.connect("./tempdata.db")
        cursor = connection.cursor()
        # Tabelle erzeugen
        sql = "CREATE TABLE tempWerte("\
            "id FLOAT, maxTempSensor FLOAT, minTempUser FLOAT, \
            maxTempUser FLOAT) " 
        cursor.execute(sql)
        connection.commit()
        connection.close()