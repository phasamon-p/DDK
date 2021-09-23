import config
import mysql.connector
from mysql.connector import Error
#from views.admin.usermanagement.user_data import *
#import services

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
        #     return connection
    except Error as e:
        return e

def selectperson():
    try:
        connection = mysqlconnect()

        sql_Select_Query = "select * from person"
        cursor = connection.cursor()
        cursor.execute(sql_Select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        rowcount = cursor.rowcount
        return [records, rowcount]

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def checkuserbyid(id):
    try:
        connection = mysqlconnect()
        print("connection ", connection)
        sql_select_Query = "SELECT * FROM person WHERE personid = %s "
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (id,))
        # get all records
        records = cursor.fetchall()
        rowcount = cursor.rowcount
        if cursor.rowcount:
            print()
            return [True, records, rowcount]
            
        else:
            return [False, records, rowcount]

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


#selectpersonbyid("OUT")