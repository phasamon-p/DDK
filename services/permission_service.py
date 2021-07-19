import config
import mysql.connector
from mysql.connector import Error
from views.admin.usermanagement.user_data import *

########################################### ABOUT CONECTION ########################################### 


def mysqlconnect():
    try:
        return mysql.connector.connect(host=config.db["host"], database=config.db["database"], user=config.db["user"], password=config.db["password"])
        # if connection.is_connected():
        #     db_Info = connection.get_server_info()
        #     print("Connected to MySQL Server version ", db_Info)
        #     cursor = connection.cursor()
        #     cursor.execute("select database();")
        #     record = cursor.fetchone()
        #     print("You're connected to database: ", record)
    except Error as e:
        return e

########################################### ABOUT FINGER PRINT ##########################################

def getfingerid():
    try:
        connection = mysqlconnect()
        sql_Select_Query = "select * from locker_count"
        cursor = connection.cursor()
        cursor.execute(sql_Select_Query)
        # get all records
        records = cursor.fetchall()
        return records[0][1]

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

            "UPDATE locker_count set count = %s where id = %s "

def updatefinrgerprint(id):
    try:
        connection = mysqlconnect()
        cursor = connection.cursor()
        mySql_update_query = "UPDATE locker_count set count = %s where id = %s "
        cursor.execute(mySql_update_query, (id, 1))
        connection.commit()

        return True

    except mysql.connector.Error as error:
        print("Failed e record: ", format(error))
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#insertperson("DDK02", "Moomud", "PP", "AS2", int(1000), "admin")
#selectperson()
#selectpersonbyid("DDK02")
#getfingerid()
#updatefinrgerprint(3)